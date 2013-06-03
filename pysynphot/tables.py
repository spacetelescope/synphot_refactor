# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
Objects that represent comp tables and graph tables.

"""

from __future__ import division, print_function
import numpy as np
import pyfits

#Flag to control verbosity
DEBUG = False


class CompTable(object):
    """
    CompTable class; opens the specified comptable and populates 1-d
    arrays of component names and file names in the members compnames
    and filenames
    """

    def __init__(self, CFile=None):
        """
        __init__ instantiates the CompTable object, given the comptable
        file name as an input string.

        Parameters
        -----------
        Input :  ndarray of chars
            string CFile containing comptable name
        Effect : ndarray of chars
            populates two data members: compnames and filenames

        """

        # None is common for various errors.
        # the default value of None is not useful; pyfits.open(None)
        # does not work.
        if CFile is None:
            raise TypeError(
                'initializing CompTable with CFile=None; possible bad/missing'
                ' CDBS')

        cp = pyfits.open(CFile)

        self.compnames = cp[1].data.field('compname')
        self.filenames = cp[1].data.field('filename')
        compdict = {}
        for i in range(len(self.compnames)):
            compdict[self.compnames[i]] = self.filenames[i]

        cp.close()
        self.name = CFile


class GraphTable(object):
    """
    GraphTable class; opens the specified graph table and populates
    1-d arrays of keyword names, innodes, outnodes and component names
    in the members keywords, innodes, outnodes and compnames

    """

    def __init__(self, GFile=None):
        """
         __init__ instantiates the GraphTable object, given the graph
        table name as an input string.

        Parameters
        ----------
        Input :  string
            GFile containing graph table name
        Effect : dict
            populates four data members::

                keywords: CharArray of keyword names
                innodes:  Int32 array of innodes
                outnodes: Int32 array of outnodes
                compnames:CharArray of components names
        """

        # None is common for various errors.
        # the default value of None is not useful;
        # pyfits.open(None) does not work.
        if GFile is None:
            raise TypeError(
                'initializing GraphTable with GFile=None; '
                'possible bad/missing CDBS')

        gp = pyfits.open(GFile)

        if 'PRIMAREA' in gp[0].header:
            self.primary_area = gp[0].header['PRIMAREA']

        self.keywords = gp[1].data.field('keyword')
        self.innodes = gp[1].data.field('innode')
        self.outnodes = gp[1].data.field('outnode')
        self.compnames = gp[1].data.field('compname')
        self.thcompnames = gp[1].data.field('thcompname')

        # keywords must be forced to lower case (STIS keywords are
        # mixed mode %^&^(*^*^%%%@#$!!!)
        for i in range(len(self.keywords)):
            self.keywords[i] = self.keywords[i].lower()


        ##        for comp in self.compnames:
        ##            try:
        ##                if comp.index('nic') == 0:
        ##                    print(comp)
        ##            except:
        ##                pass

        # prints components associated with a given keyword
        ##        i = -1
        ##        for keyword in self.keywords:
        ##            i = i + 1
        ##            if keyword == 'acs':
        ##                print(self.compnames[i])

        gp.close()

    def GetNextNode(self, modes, innode):
        '''GetNextNode returns the outnode that matches an element from
        the modes list, starting at the given innode.
        This method isnt actually used, its just a helper method for
        debugging purposes'''
        nodes = np.where(self.innodes == innode)

        ## If there's no entry for the given innode, return -1
        if nodes[0].size == 0:
            return -1

        ## If we don't match anything in the modes list, we find the
        ## outnode corresponding the the string 'default'
        defaultindex = np.where(self.keywords[nodes] == 'default')

        if len(defaultindex[0]) != 0:
            outnode = self.outnodes[nodes[0][defaultindex[0]]]

        ## Now try and match one of the strings in the modes list with
        ## the keywords corresponding to the list of entries with the given
        ## innode
        for mode in modes:
            result = self.keywords[nodes].count(mode)
            if result != 0:
                index = np.where(self.keywords[nodes] == mode)
                outnode = self.outnodes[nodes[0][index[0]]]

        ## Return the outnode corresponding either to the matched mode,
        ## or to 'default'
        return outnode

    def GetComponentsFromGT(self, modes, innode):
        """
        GetComponentsFromGT returns two lists of component names
        corresponding to those obtained by waling down the graph
        table starting at innode. The first list contains the optical
        components, the second list, the thermal components.

        """

        components = []
        thcomponents = []
        outnode = 0
        inmodes = set(modes)
        used_modes = set()
        count = 0
        while outnode >= 0:
            if (DEBUG and (outnode < 0)):
                print("outnode == {0:d}: stop condition".fortmat(outnode))

            previous_outnode = outnode

            nodes = np.where(self.innodes == innode)

            # If there are no entries with this innode, we're done
            if nodes[0].size == 0:
                if DEBUG:
                    print("no such innode {0:d}: stop condition".format(innode))
                    #return (components,thcomponents)
                break

            # Find the entry corresponding to the component named
            # 'default', bacause thats the one we'll use if we don't
            # match anything in the modes list
            defaultindex = np.where(self.keywords[nodes] == 'default')

            if 'default' in self.keywords[nodes]:
                dfi = np.where(self.keywords[nodes] == 'default')[0][0]
                outnode = self.outnodes[nodes[0][dfi]]
                component = self.compnames[nodes[0][dfi]]
                thcomponent = self.thcompnames[nodes[0][dfi]]
                used_default = True
            else:
                #There's no default, so fail if you don't match anything
                # in the keyword matching step.
                outnode = -2
                component = thcomponent = None

            # Now try and match something from the modes list
            for mode in modes:

                if mode in self.keywords[nodes]:
                    used_modes.add(mode)
                    index = np.where(self.keywords[nodes] == mode)
                    if len(index[0]) > 1:
                        raise KeyError(
                            '%d matches found for %s' % (len(index[0]), mode))
                    idx = index[0][0]
                    component = self.compnames[nodes[0][idx]]
                    thcomponent = self.thcompnames[nodes[0][idx]]
                    outnode = self.outnodes[nodes[0][idx]]
                    used_default = False

            if DEBUG:
                print("Innode {0:d}  Outnode {1:d}  Compname {2:s}".format(
                    innode, outnode, component))
            components.append(component)
            thcomponents.append(thcomponent)

            innode = outnode

            if outnode == previous_outnode:
                if DEBUG:
                    print("Innode: {0:d}  Outnode:{1:d}  "
                          "Used default: {2:s}".format(innode,
                                                       outnode,
                                                       used_default))
                count += 1
                if count > 3:
                    if DEBUG:
                        print("same outnode {0:d} > 3 times: stop "
                              "condition".format(outnode))
                    break

        if outnode < 0:
            if DEBUG:
                print("outnode == {0:d}: stop condition".format(outnode))
            raise ValueError("Incomplete obsmode {0:s}".format(modes))

        #Check for unused modes
        if inmodes != used_modes:
            unused = str(inmodes.difference(used_modes))
            raise ValueError("Warning: unused keywords {0:s}".format(unused))

        return components, thcomponents
