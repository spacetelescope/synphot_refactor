# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
Graph table re-implementation
Data structure & traversal algorithm suggested by Alex Martelli,
http://stackoverflow.com/questions/844505/is-a-graph-library-eg-networkx-the-right-solution-for-my-python-problem

"""

from __future__ import division, print_function
from collections import defaultdict
import pyfits


class GraphNode(object):
    """
    Structure to hold all the information associated with a single
    innode of the graph table. The constructor produces an empty node,
    which must be filled later.
    This structure will be the value associated with the GraphTab dict.

    """

    def __init__(self):
        """
        ( (default_outnode, compname, thcompname),
              {'kwd':(outnode, compname, thcompname)} )

        """
        self.default = (None, None, None)
        self.named = {}
        self.entry = (self.default, self.named)

    def __repr__(self):
        """
        Maybe change this

        """
        return str((self.default, self.named))

    def set_default(self, outnode, compname, thcompname):
        self.default = (outnode, compname, thcompname)
        self.entry = (self.default, self.named)

    def set_named(self, kwd, outnode, compname, thcompname):
        if kwd in self.named:
            raise IndexError("%s entry already exists for this node"%kwd)
        else:
            self.named[kwd]=(outnode, compname, thcompname)
            self.entry = (self.default, self.named)

    def get_default(self):
        return self.default

    def get_named(self, kwd):
        return self.named[kwd]


class GraphPath(object):
    """
    Simple class containing the result of a traversal of the GraphTable

    """

    def __init__(self, obsmode_string, optical, thermal, params, tname):
        """
        Parameters
        -----------
        optical: list of strings
            optical component names
        thermal: list of strings
            thermal component names
        params: dict
            dictionary of {compname:parameterized value} for
                     any parameterized keywords used in the obsmode string

        """
        self.obsmode = obsmode_string
        self.optical = optical
        self.thermal = thermal
        self.params = params
        self.gtable = tname

    def __repr__(self):
        return str((self.optical, self.thermal, self.params, self.gtable))

    def __len__(self):
        return max(len(self.optical),
                   len(self.thermal))


class GraphTable(object):
    def __init__(self, fname):
        self.tab = defaultdict(GraphNode)
        self.tname = fname
        self.problemset = set()
        self.inittab()

        if self.problemset:
            print("warning, ambiguous nodes encountered")
            print("(innode, kwd, (outnode, compname, thcompname)")
            for k in self.problemset:
                print(k)

        self.all_nodes = set()
        for node in self.tab:
            self.all_nodes.add(node)
            self.add_descendants(node, self.all_nodes)

    def inittab(self):
        # Both FITS files and text files are supported
        # In either case, process one row at a time
        if self.tname.endswith('.fits'):
            f = pyfits.open(self.tname)

            if 'PRIMAREA' in f[0].header:
                self.primary_area = f[0].header['PRIMAREA']

            for row in f[1].data:
                if not row.field('compname').endswith('graph'):
                    # Make it a list because FITS_records don't fully
                    # implement all the usual sequence behaviors
                    self._setrow(list(row))
                else:
                    raise NotImplementedError('Segmented graph tables not yet '
                                              'supported')
            f.close()
        else:  # Not a FITS file; assume text
            f = open(self.tname)
            for line in f:
                try:
                    row = line.split()
                except ValueError as e:
                    print("Error parsing line ", line)
                    raise e
                self._setrow(row)
            f.close()

    def _setrow(self, row):
        """
        Parameters
        ----------
        row: a list or tuple
             the list or tuple containing ordered elements::

                kwd, innode, outnode, compname, thcomp

            followed by comments & other ignored things

        """
        try:
            compname, kwd, innode, outnode, thcomp = row[0:5]
        except ValueError:
            raise ValueError('Error unpacking row: %s' % row)

        # Innode is an integer
        k = int(innode)

        # "Clear" should become None
        if compname == 'clear':
            compname = None
        if thcomp == 'clear':
            thcomp = None

        # Now create the GraphNode defined by this row,
        # and add it to the table. Default nodes are special.
        if kwd == 'default':
            self.tab[k].set_default(int(outnode), compname, thcomp)
        else:
            try:
                self.tab[k].set_named(kwd, int(outnode), compname, thcomp)
            except IndexError:
                old = self.tab[k].get_named(kwd)
                plist = (k, kwd, old, (outnode, compname, thcomp))
                self.problemset.add(plist)

    def traverse(self, icss, verbose=False):
        opt = []
        thm = []
        used = set()
        paramcomp = dict()
        nodelist = list()

        # Returns a list of keywords and a dict of paramkeys
        kws, paramdict = extract_keywords(icss)
        if verbose:
            print(kws)
            print(paramdict)
        # Always start with innode=1
        nextnode = 1

        # Keep going as long as the next node is in this table
        while nextnode in self.tab:
            defnode = self.tab[nextnode].default
            othernodes = self.tab[nextnode].named

            # Check if the keywords match a named option
            found = kws & set(othernodes)

            if found:
                if verbose:
                    print(found)
                # ...and that we don't have ambiguity
                if len(found) == 1:
                    used.update(found)
                    matchkey = found.pop()
                    matchnode = othernodes[matchkey]
                else:
                    raise ValueError("Invalid obsmode: cannot use %s together"
                                     % found)
            else:
                # fall back to default
                matchnode = defnode

            # Having picked out the matching node, also pick up
            # the optical & thermal components from it
            nodelist.append(matchnode)
            nextnode, ocomp, tcomp = matchnode
            if ocomp is not None:
                opt.append(ocomp)
            if tcomp is not None:
                thm.append(tcomp)

            # Special handling of paramterization
            if matchkey in paramdict:
                paramcomp[ocomp] = float(paramdict[matchkey])
                paramcomp[tcomp] = float(paramdict[matchkey])

            if verbose:
                print(matchnode)

            if nextnode is None:
                raise ValueError("Incomplete obsmode: legal possibilities %s" %
                                 str(othernodes.keys()))

        # We're done with the table. If there are any keywords left over,
        # raise an exception.
        if kws != used:
            raise ValueError("Unused keywords %s" %
                             str([k for k in (kws-used)]))

        # The results are returned as a simple class
        path = GraphPath(icss, opt, thm, paramcomp, self.tname)
        return path

# Helper/validation methods, should be marked private
    def add_descendants(self, node, updateset=None):
        """
        auxiliary function: add all descendants of node to someset

        """
        someset = set()
        startnode = self.tab[node]

        defout = startnode.default[0]
        if defout is not None:
            someset.add(defout)
        for kwd, matchnode in startnode.named.items():
            if matchnode[0] is not None:
                someset.add(matchnode[0])

        if someset is not None:
            updateset.update(someset)
        else:
            return someset

    def validate(self):
        """
        Simulataneously checks for loops and unreachable nodes

        """
        msg = list()
        previously_seen = set()
        currently_seen = set([1])
        problemset = set()
        while currently_seen:
            node = currently_seen.pop()
            if node in previously_seen:
                problemset.add(node)
            else:
                previously_seen.add(node)
                self.add_descendants(node, currently_seen)

        unreachable = self.all_nodes - previously_seen
        if unreachable:
            msg.append("%d unreachable nodes: " % len(unreachable))
            for node in unreachable:
                msg.append(str(node))

        if problemset:
            msg.append("Loop involving %d nodes" % len(problemset))
            for node in problemset:
                msg.append(str(node))

        if msg:
            return msg
        else:
            return True


def extract_keywords(icss):
    """
    Helper function

        Parameters
        ----------
        icss: string
            comma-separated string

        Returns
        -------
        kws: list of string
            set of keywords
        paramdict: dict
            dict of {parameterized_keyword: parameter_value}

    """
    # Force to lower case & split into keywords
    kws = set(icss.lower().split(','))

    # parameterized keywords require special handling
    paramdict = {}
    parlist = [k for k in kws if '#' in k]
    for k in parlist:
        key, val = k.split('#')
        # Take the parameterized value off the keyword...
        kws.remove(k)
        kws.add(key+'#')
        # ...and save it in the dictionary
        paramdict[key+'#'] = val
    return kws, paramdict


class CompTable(object):
    """
    This class will cooperate with a GraphPath to produce a
    realized list of files

    """

    def __init__(self, fname):
        self.tab = dict()
        self.tname = fname
        self.inittab()

    def __getitem__(self, key):
        return self.tab[key]

    def inittab(self):
        # Support fits or text files
        # Should the filenames be converted at this point, or later?
        if self.tname.endswith('.fits'):
            f = pyfits.open(self.tname)
            for row in f[1].data:
                self.tab[row.field('compname')] = row.field('filename')
            f.close()
        else:
            #Only simple text file supported
            f = open(self.tname)
            for line in f:
                compname, filename = line.split()
                self.tab[compname] = filename
            f.close()
