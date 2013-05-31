# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This module defines classes used to define reddening laws and
extinctions.

"""

from __future__ import division, print_function
import pyfits
from spectrum import ArraySpectralElement
import Cache
import extinction  # temporary(?) backwards compatibility


class CustomRedLaw(object):
    def __init__(self,
                 wave=None,
                 waveunits='InverseMicrons',
                 Avscaled=None,
                 name='Unknown Reddening Law',
                 litref=None):

        self.wave = wave
        self.waveunits = waveunits
        self.obscuration = Avscaled
        self.name = name
        self.litref = litref

    def reddening(self, extval):
        """
        Compute the reddening for the provided value of the extinction.

        """
        T = 10.0**(-0.4*extval*self.obscuration)
        ans = ArraySpectralElement(wave=self.wave,
                                   waveunits=self.waveunits,
                                   throughput=T,
                                   name='%s(Av=%g)' % (self.name, extval)
                                   )
        ans.citation = self.litref
        return ans


class RedLaw(CustomRedLaw):
    """
    Defines a reddening law from a FITS file.

    """
    def __init__(self, filename):
        f = pyfits.open(filename)
        d = f[1].data
        CustomRedLaw.__init__(self,
                              wave=d.field('wavelength'),
                              waveunits=f[1].header['tunit1'],
                              Avscaled=d.field('Av/E(B-V)'),
                              litref=f[0].header['litref'],
                              name=f[0].header['shortnm'])
        f.close()


def print_red_laws():
    """
    Print information regarding the extinction laws currently available
    on CDBS. The printed names may be used with the Extinction function
    to retrieve available reddening laws.

    """
    laws = {}

    # start by converting the Cache.RedLaws file names to RedLaw objects
    # if they aren't already
    for k in Cache.RedLaws:
        if isinstance(Cache.RedLaws[k], str):
            Cache.RedLaws[k] = RedLaw(Cache.RedLaws[k])

        laws[str(k)] = Cache.RedLaws[k].litref

    # get the length of the longest name and litref
    maxname = max([len(name) for name in laws.keys()])
    maxref = max([len(ref) for ref in laws.values()])

    s = '%-' + str(maxname) + 's   %-' + str(maxref) + 's'

    print(s % ('name', 'reference'))
    print(s % ('-'*maxname, '-'*maxref))

    for k in sorted(laws.keys()):
        print(s % (k, laws[k]))


def Extinction(extval, name=None):
    """
    extinction = Extinction(extinction (E(B-V)) in magnitudes,
                           'reddening law')

    If no name is provided, the average Milky Way extinction will
    be used. Run the print_red_laws function to see available names.

    """
    try:
        ext = Cache.RedLaws[name].reddening(extval)
    except AttributeError:
        # The cache hasn't yet been filled.
        Cache.RedLaws[name] = RedLaw(Cache.RedLaws[name])
        ext = Cache.RedLaws[name].reddening(extval)
    except KeyError:
        # There's no reddening law by that name. See if we've been
        # given a filename from which we can read one.
        try:
            Cache.RedLaws[name] = RedLaw(name)
            ext = Cache.RedLaws[name].reddening(extval)
        except IOError:
            # If not, see if it's an old extinction law
            try:
                ext = extinction.DeprecatedExtinction(extval, name)
            except KeyError:
                raise ValueError('No extinction law has been defined for "%s", '
                                 'and no such file exists' % name)
    return ext
