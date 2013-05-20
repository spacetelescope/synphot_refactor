# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import division

"""
Module: spectrum.py

Contains SourceSpectrum and SpectralElement class definitions and
their subclasses.

Also contains the Vega object, which is an instance of a FileSourceSpectrum
that can be imported from this file and used for Vega-related calculations.

:Dependencies:
pyfits, numpy


"""

import re
import os
import math
import warnings

import pyfits
import numpy as np

import refs
import units
import locations
import planck
import pysynphot.exceptions as exceptions  # custom pysyn exceptions

from pysynphot import __version__
try :
    from pysynphot import __svn_revision__
except ImportError:
    __svn_revision__ = 'unk'

# Renormalization constants from synphot:
PI = 3.14159265               # Mysterious math constant
RSUN = 6.9599E10              # Radius of sun
PC = 3.085678E18              # Parsec
RADIAN = RSUN / PC /1000.
RENORM = PI * RADIAN * RADIAN  # Normalize to 1 solar radius @ 1 kpc

# MergeWaveSets "too close together" constant
MERGETHRESH = 1.e-12

#Single-precision epsilon value, taken from the synphot FAQ.
#This is the minimum separation in wavelength value necessary for
#synphot to read the entries as distinct single-precision numbers.
syn_epsilon = 0.00032


def MergeWaveSets(waveset1, waveset2):
    """
    Return the union of the two wavesets, unless one or
    both of them is None.

    """
    if waveset1 is None and waveset2 is not None:
        MergedWaveSet = waveset2
    elif waveset2 is None and waveset1 is not None:
        MergedWaveSet = waveset1
    elif waveset1 is None and Waveset2 is None:
        MergedWaveSet = None
    else:
        MergedWaveSet = np.union1d(waveset1, waveset2)

        # The merged wave sets may sometimes contain numbers which are nearly
        # equal but differ at levels as small as 1e-14. Having values this
        # close together can cause problems down the line so here we test whether
        # any such small differences are present, with a small difference
        # defined as less than MERGETHRESH.
        #
        # If small differences are present we make a copy of the union'ed array
        # with the lower of the close together pairs removed.
        delta = MergedWaveSet[1:] - MergedWaveSet[:-1]

        if not (delta > MERGETHRESH).all():
            newlen = len(delta[delta > MERGETHRESH]) + 1
            newmerged = np.zeros(newlen,dtype=MergedWaveSet.dtype)
            newmerged[:-1] = MergedWaveSet[delta > MERGETHRESH]
            newmerged[-1] = MergedWaveSet[-1]

            MergedWaveSet = newmerged

    return MergedWaveSet


def trimSpectrum(sp, minw, maxw):
    """
    Creates a new spectrum with trimmed upper and lower ranges.

    """
    wave = sp.GetWaveSet()
    flux = sp(wave)

    new_wave = np.compress(wave >= minw, wave)
    new_flux = np.compress(wave >= minw, flux)

    new_wave = np.compress(new_wave <= maxw, new_wave)
    new_flux = np.compress(new_wave <= maxw, new_flux)

    result = TabularSourceSpectrum()

    result._wavetable = new_wave
    result._fluxtable = new_flux

    result.waveunits = units.Units(sp.waveunits.name)
    result.fluxunits = units.Units(sp.fluxunits.name)

    return result


class Integrator(object):
    """
    Integrator engine.

    """
    def trapezoidIntegration(self, x, y):
        npoints = x.size
        if npoints > 0:
            indices = np.arange(npoints)[:-1]
            deltas = x[indices+1] - x[indices]
            integrand = 0.5*(y[indices+1] + y[indices])*deltas
            sum = integrand.sum()
            if x[-1]<x[0]:
                sum *= -1.0
            return sum
        else:
            return 0.0

    def _columnsFromASCII(self, filename):
        """
        Following synphot/TABLES, ASCII files may contain blank lines,
        comment lines (beginning with '#'), or terminal comments. This routine
        may be called by both Spectrum and SpectralElement objects to extract
        the first two columns from a file.

        """

        wlist = []
        flist = []
        lcount = 0
        fs = open(filename, mode='r')
        lines = fs.readlines()
        fs.close()
        for line in lines:
            lcount += 1
            cline = line.strip()
            if len(cline) > 0 and not cline.startswith('#'):
                try:
                    cols = cline.split()
                    if len(cols) >= 2:
                        wlist.append(float(cols[0]))
                        flist.append(float(cols[1]))
                except Exception as e:
                    raise exceptions.BadRow("Error reading %s: %s" % (filename,
                                            str(e)),
                                            rows=lcount
                                            )
        return wlist, flist

    def validate_wavetable(self):
        """
        Enforce monotonic, ascending wavelengths with no zero values

        """
        #First check for invalid values
        wave = self._wavetable
        if np.any(wave <= 0):
            wrong=np.where(wave <= 0)[0]
            raise exceptions.ZeroWavelength('Negative or Zero wavelength '
                                            'occurs in wavelength array',
                                            rows=wrong
                                            )

        #Now check for monotonicity & enforce ascending
        sorted = np.sort(wave)
        if not np.alltrue(sorted == wave):
            if np.alltrue(sorted[::-1] == wave):
                #monotonic descending is allowed
                pass
            else:
                wrong = np.where(sorted != wave)[0]
                raise exceptions.UnsortedWavelength('Wavelength array is not '
                                                    'monotonic', rows=wrong
                                                    )
        #Check for duplicate values
        dw = sorted[1:]-sorted[:-1]
        if np.any(dw==0):
            wrong = np.where(dw==0)[0]
            raise exceptions.DuplicateWavelength("Wavelength array contains "
                                                 "duplicate entries",
                                                 rows=wrong
                                                )

    def validate_fluxtable(self):
        """
        Enforce non-negative fluxes

        """
        if not self.fluxunits.isMag and self._fluxtable.min() < 0:
            # neg. magnitudes are legal
            idx=np.where(self._fluxtable < 0)
            self._fluxtable[idx]=0.0
            print "Warning, %d of %d bins contained negative fluxes; " \
                  "they have been set to zero." % \
                  (len(idx[0]), len(self._fluxtable))


class SourceSpectrum(Integrator):
    """
    Base class for the Source Spectrum object.

    """

    wave = property(_getWaveProp, doc="Wavelength property")
    flux = property(_getFluxProp, doc="Flux property")

    def __add__(self, other):
        """
        Source Spectra can be added.  Delegate the work to the
        CompositeSourceSpectrum class.

        """
        if not isinstance(other, SourceSpectrum):
            raise TypeError("Can only add two SourceSpectrum objects")

        return CompositeSourceSpectrum(self, other, 'add')

    def __sub__(self, other):
        """
        Source Spectra can be subtracted, which is just another way
        of adding.

        """

        return self.__add__(-1.0*other)

    def __mul__(self, other):
        """
        Source Spectra can be multiplied, by constants or by
        SpectralElement objects.

        """
        # Multiplying by numeric constants is allowed
        if isinstance(other, (int, float)):
            other = UniformTransmission(other)
        #so is by SpectralElements. Otherwise, raise an exception.
        if not isinstance(other, SpectralElement):
            raise TypeError("SourceSpectrum objects can only be multiplied "
                            "by SpectralElement objects or constants; "
                            "%s type detected" % type(other))


        # Delegate the work of multiplying to CompositeSourceSpectrum
        return CompositeSourceSpectrum(self, other, 'multiply')

    def __rmul__(self, other):
        return self.__mul__(other)

    def addmag(self, magval):
        """
        Adding a magnitude is like multiplying a flux. Only works for
        numbers -- not arrays, spectrum objects, etc

        """
        if np.isscalar(magval):
            factor = 10**(-0.4*magval)
            return self*factor
        else:
            raise TypeError(".addmag() only takes a constant scalar argument")

    def getArrays(self):
        """
        Returns wavelength and flux arrays as a tuple, performing
        units conversion.

        """
        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        wave = self.GetWaveSet()
        flux = self(wave)

        flux = units.Photlam().Convert(wave, flux, self.fluxunits.name,
                                       area=area)
        wave = units.Angstrom().Convert(wave, self.waveunits.name)
        return wave, flux

    # Define properties for consistent UI
    def _getWaveProp(self):
        wave, flux = self.getArrays()
        return wave

    def _getFluxProp(self):
        wave,flux = self.getArrays()
        return flux

    def validate_units(self):
        """
        Ensure that waveunits are WaveUnits and fluxunits are FluxUnits

        """
        if not isinstance(self.waveunits, units.WaveUnits):
            raise TypeError("%s is not a valid WaveUnit" % self.waveunits)
        if not isinstance(self.fluxunits,units.FluxUnits):
            raise TypeError("%s is not a valid FluxUnit" % self.fluxunits)

    def writefits(self, filename, clobber=True, trimzero=True,
                  binned=False, precision=None, hkeys=None):
        """
        Write the spectrum to a FITS file.

        Parameters
        ----------
        filename : string
            name of file to write to
        clobber : bool [Default: True]
            Will clobber existing file by default
        trimzero : bool [Default:True]
            Will trim zero-flux elements from both ends by default
        binned : bool [Default: False]
            Will write in native waveset by default
        precision : {'single','double', None}
            Will write in native precision by default
        hkeys :  dict
            Optional dictionary of {keyword:(value,comment)} to be added to primary FITS header

        """

        if precision is None:
            precision = self.flux.dtype.char
        _precision = precision.lower()[0]

        pcodes = {'d': 'D', 's': 'E', 'f': 'E'}

        if clobber:
            try:
                os.remove(filename)
            except OSError:
                pass

        if binned:
            wave = self.binwave
            flux = self.binflux
        else:
            wave = self.wave
            flux = self.flux

        # Add a check for single/double precision clash, so
        # that if written out in single precision, the wavelength table
        # will still be sorted with no duplicates
        # The value of epsilon is taken from the Synphot FAQ.

        if wave.dtype == np.float64 and _precision == 's':
            idx = np.where(abs(wave[1:]-wave[:-1]) > syn_epsilon)
        else:
            idx = np.where(wave)  # => idx=[:]

        wave = wave[idx]
        flux = flux[idx]

        first, last = 0, len(flux)

        if trimzero:
            # Keep one zero at each end
            nz = flux.nonzero()[0]
            try:
                first = max(nz[0]-1, first)
                last = min(nz[-1]+2, last)
            except IndexError:
                pass

        #Construct the columns and HDUlist
        cw = pyfits.Column(name='WAVELENGTH',
                           array=wave[first:last],
                           unit=self.waveunits.name,
                           format=pcodes[_precision])
        cf = pyfits.Column(name='FLUX',
                           array=flux[first:last],
                           unit=self.fluxunits.name,
                           format=pcodes[_precision])

        # Make the primary header
        hdu = pyfits.PrimaryHDU()
        hdulist = pyfits.HDUList([hdu])

        # User-provided keys are written to the primary header
        # so are filename and origin
        bkeys = dict(filename=(os.path.basename(filename), 'name of file'),
                     origin=('pysynphot',
                             'Version (%s, %s)' % (__version__,
                                                   __svn_revision__)))

        # User-values if present may override default values
        if hkeys is not None:
            bkeys.update(hkeys)

        # Now update the primary header
        for key, val in bkeys.items():
            hdu.header.update(key, *val)

        # Make the extension HDU
        cols = pyfits.ColDefs([cw, cf])
        hdu = pyfits.new_table(cols)

        # There are some standard keywords that should be added
        # to the extension header.
        bkeys = dict(expr=(str(self), 'pysyn expression'), tdisp1 = ('G15.7', ),
                     tdisp2 = ('G15.7',)
                    )

        try:
            bkeys['grftable'] = (self.bandpass.obsmode.gtname,)
            bkeys['cmptable'] = (self.bandpass.obsmode.ctname,)
        except AttributeError as e:
            pass  # Not all spectra have these

        for key, val in bkeys.items():
            hdu.header.update(key, *val)

        # Add the header to the list, and write the file
        hdulist.append(hdu)
        hdulist.writeto(filename)

    def integrate(self, fluxunits='photlam'):
        # Extract the flux in the desired units
        u = self.fluxunits
        self.convert(fluxunits)
        wave, flux = self.getArrays()
        self.convert(u)
        #then do the integration
        return self.trapezoidIntegration(wave, flux)

    def sample(self, wave, interp=True):
        """
        Return a flux array, in self.fluxunits, on the provided
        wavetable

        """

        if interp:
            # convert input wavelengths to Angstroms since the __call__ method
            # will be expecting that
            angwave = self.waveunits.ToAngstrom(wave)

            #First use the __call__ to get it in photlam
            flux = self(angwave)

            if hasattr(self, 'primary_area'):
                area = self.primary_area
            else:
                area = None

            #Then convert to the desired units
            ans = units.Photlam().Convert(angwave, flux,
                                          self.fluxunits.name, area=area)

        else:
            # Get the arrays in the proper units
            wave_array, flux_array = self.getArrays()
            if np.isscalar(wave):
                # Find the correct index
                diff = abs(wave-wave_array)
                idx = diff.argmin()

                ans = flux_array[idx]

            else:
                raise NotImplementedError("Interp=False not yet supported for non-scalars")

        return ans

    def convert(self, targetunits):
        '''Convert to other units. This method actually just changes the
        wavelength and flux units objects, it does not recompute the
        internally kept wave and flux data; these are kept always in internal
        units. Method getArrays does the actual computation.
        '''
        nunits = units.Units(targetunits)

        if nunits.isFlux:
            self.fluxunits = nunits
        else:
            self.waveunits = nunits

    def redshift(self, z):
        ''' Returns a new redshifted spectrum.
        '''
        #By default, apply only the doppler shift.

        waveunits=self.waveunits
        self.convert('angstrom')
        newwave=self.wave*(1.0+z)
        copy = ArraySourceSpectrum(wave=newwave,
                             flux=self.flux,
                             waveunits=self.waveunits,
                             fluxunits=self.fluxunits,
                             name="%s at z=%g"%(self.name,z)
                             )

        self.convert(waveunits)
        return copy

    def setMagnitude(self, band, value):
        '''Makes the magnitude of the source in the band equal to value.
        band is a SpectralElement.
        This method is marked for deletion once the .renorm method is
        well tested.
        '''
        objectFlux = band.calcTotalFlux(self)
        vegaFlux = band.calcVegaFlux()
        magDiff = -2.5*math.log10(objectFlux/vegaFlux)
        factor = 10**(-0.4*(value - magDiff))

        '''Object returned is a CompositeSourceSpectrum'''

        return self * factor

    def renorm(self, RNval, RNUnits, band, force=False):
        """Renormalize the spectrum to the specified value (in the specified
        flux units) in the specified band.
        Calls a function in another module to alleviate circular import
        issues."""

        from renorm import StdRenorm
        return StdRenorm(self,band,RNval,RNUnits,force=force)

    def effstim(self,fluxunits='photlam'):
        print "?? %s"%fluxunits
        raise NotImplementedError("Ticket #140: calcphot.effstim functionality")

class CompositeSourceSpectrum(SourceSpectrum):
    '''Composite Source Spectrum object, handles addition, multiplication
    and keeping track of the wavelength set.
    '''
    def __init__(self, source1, source2, operation):
        self.component1 = source1
        self.component2 = source2
        self.operation = operation

        self.name = str(self)

        #Propagate warnings
        self.warnings={}
        self.warnings.update(source1.warnings)
        self.warnings.update(source2.warnings)

        # for now we keep these attributes here, in spite of the internal
        # units model. There is code that still breaks down if these attributes
        # are not here.
        try:
            self.waveunits = source1.waveunits
            self.fluxunits = source1.fluxunits
        except AttributeError:
            self.waveunits = source2.waveunits
            self.fluxunits = source2.fluxunits

        self.isAnalytic = source1.isAnalytic and source2.isAnalytic

        # check areas
        if hasattr(source1, 'primary_area'):
            source1_area = source1.primary_area
        else:
            source1_area = None

        if hasattr(source2, 'primary_area'):
            source2_area = source2.primary_area
        else:
            source2_area = None

        if not source1_area and not source2_area:
            self.primary_area = None

        elif source1_area and not source2_area:
            self.primary_area = source1_area

        elif not source1_area and source2_area:
            self.primary_area = source2_area

        else:
            if source1_area == source2_area:
                self.primary_area = source1_area

            else:
                err = 'Components have different area attributes: %s: %f, %s: %f'
                err = err % (str(source1), source1_area,
                             str(source2), source2_area)
                raise exceptions.IncompatibleSources(err)

    def __str__(self):
        opdict = {'add':'+','multiply':'*'}
        return "%s %s %s" % (str(self.component1),opdict[self.operation],str(self.component2))

    def __call__(self, wavelength):
        '''Add or multiply components, delegating the function calculation
        to the individual objects.
        '''
        if self.operation == 'add':
            return self.component1(wavelength) + self.component2(wavelength)

        if self.operation == 'multiply':
            return self.component1(wavelength) * self.component2(wavelength)

    def __iter__(self):
        """ Allow iteration over each component. """

        complist = self.complist()
        return complist.__iter__()

    def complist(self):
        ans=[]
        for comp in (self.component1, self.component2):
            try:
                ans.extend(comp.complist())
            except AttributeError:
                ans.append(comp)
        return ans

    def GetWaveSet(self):
        '''Obtain the wavelength set for the composite source by forming
        the union of wavelengths from each component.
        '''
        waveset1 = self.component1.GetWaveSet()
        waveset2 = self.component2.GetWaveSet()

        return MergeWaveSets(waveset1, waveset2)

    def tabulate(self):
        """Evaluate the spectrum in order to return a tabular source
        spectrum"""
        sp=ArraySourceSpectrum(wave=self.wave,
                               flux=self.flux,
                               waveunits=self.waveunits,
                               fluxunits=self.fluxunits,
                               name='%s (tabulated)'%self.name)
        return sp

class TabularSourceSpectrum(SourceSpectrum):
    '''Class for a source spectrum that is read in from a table.
    '''
    def __init__(self, filename=None, fluxname=None, keepneg=False):
        self.isAnalytic=False
        self.warnings={}
        if filename:
            self._readSpectrumFile(filename, fluxname)
            self.filename=filename
            self.validate_units()
            self.validate_wavetable()
            if not keepneg:
                self.validate_fluxtable()
            self.ToInternal()
            self.name=self.filename
            self.isAnalytic=False
        else:
            self._wavetable = None
            self._fluxtable = None
            self.waveunits = None
            self.fluxunits = None
            self.filename = None
            self.name=self.filename

    def _reverse_wave(self):
        self._wavetable = self._wavetable[::-1]


    def __str__(self):
        return str(self.name)

    def _readSpectrumFile(self, filename, fluxname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, fluxname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, fluxname):
        fs = pyfits.open(filename)

        self._wavetable = fs[1].data.field('wavelength')
        if fluxname == None:
            fluxname = 'flux'
        self._fluxtable = fs[1].data.field(fluxname)

        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.fluxunits = units.Units(fs[1].header['tunit2'].lower())

        fs.close()

    def _readASCII(self, filename):
        """ Ascii files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is flux in Flam."""

        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('flam')
        wlist,flist = self._columnsFromASCII(filename)
        self._wavetable=np.array(wlist,dtype=np.float64)
        self._fluxtable=np.array(flist,dtype=np.float64)


    def __call__(self, wavelengths):
        '''This is where the flux array is actually calculated given a
        wavelength array. Returns an array of flux values calculated at
        the wavelength values input.
        '''
        if np.isscalar(wavelengths):
            delta=0.0001
            ww=np.array([wavelengths-delta,wavelengths,wavelengths+delta])
            tmp=self.resample(ww)
            return tmp._fluxtable[1]
        else:
            return self.resample(wavelengths)._fluxtable





    def taper(self):
        '''Taper the spectrum by adding zeros to each end.
        '''
        OutSpec = TabularSourceSpectrum()
        wcopy = np.zeros(self._wavetable.size+2,dtype=np.float64)
        fcopy = np.zeros(self._fluxtable.size+2,dtype=np.float64)
        wcopy[1:-1] = self._wavetable
        fcopy[1:-1] = self._fluxtable
        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        ## The wavelengths to use for the first and last points are
        ## calculated by using the same ratio as for the 2 interior points
        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutSpec._wavetable = wcopy
        OutSpec._fluxtable = fcopy
        OutSpec.waveunits = units.Units(str(self.waveunits))
        OutSpec.fluxunits = units.Units(str(self.fluxunits))

        return OutSpec

    def resample(self, resampledWaveTab):
        '''Interpolate flux given a wavelength array that is monotonically
        increasing and the TabularSourceSpectrum object.

        Parameters
        ----------
        resampledWaveTab : ndarray
            new wavelength table IN ANGSTROMS

        '''

        ##Check whether the input wavetab is in descending order
        if resampledWaveTab[0]<resampledWaveTab[-1]:
            newwave=resampledWaveTab
            newasc = True
        else:
            newwave=resampledWaveTab[::-1]
            newasc = False

        ## Use numpy interpolation function
        if self._wavetable[0]<self._wavetable[-1]:
            oldasc = True
            ans = np.interp(newwave,self._wavetable,
                           self._fluxtable)
        else:
            oldasc = False
            rev = np.interp(newwave,self._wavetable[::-1],
                           self._fluxtable[::-1])
            ans = rev[::-1]


        ## If the new and old waveset don't have the same parity,
        ## the answer has to be flipped again
        if (newasc != oldasc):
            ans=ans[::-1]

        ## Finally, make the new object
        # NB: these manipulations were done using the internal
        #tables in Angstrom and photlam, so those are the units
        #that must be fed to the constructor.
        resampled=ArraySourceSpectrum(wave=resampledWaveTab.copy(),
                                      waveunits = 'angstroms',
                                      flux = ans.copy(),
                                      fluxunits = 'photlam',
                                      keepneg=True)

        #Use the convert method to set the units desired by the user.
        resampled.convert(self.waveunits)
        resampled.convert(self.fluxunits)

        return resampled

    def GetWaveSet(self):
        '''For a TabularSource Spectrum, the WaveSet is just the _wavetable
        member.  Return a copy so that there is no reference to the original
        object.
        '''
        return self._wavetable.copy()

    def ToInternal(self):
        '''Convert to the internal representation of (angstroms, photlam).
        '''
        self.validate_units()

        savewunits = self.waveunits
        savefunits = self.fluxunits

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        angwave = self.waveunits.Convert(self.GetWaveSet(), 'angstrom')
        phoflux = self.fluxunits.Convert(angwave, self._fluxtable, 'photlam',
                                          area=area)

        self._wavetable = angwave.copy()
        self._fluxtable = phoflux.copy()

        self.waveunits = savewunits
        self.fluxunits = savefunits

class ArraySourceSpectrum(TabularSourceSpectrum):
    """Create a spectrum from arrays.

    spec = ArraySpectrum(numpy array containing wavelength table,
    numpy array containing flux table, waveunits, fluxunits,
    name=human-readable nickname for spectrum, keepneg=True to
    override the default behavior of setting negative flux values to zero)
    """
    def __init__(self, wave=None, flux=None,
                 waveunits='angstrom', fluxunits='photlam',
                 name='UnnamedArraySpectrum',
                 keepneg=False):
        """

        Parameters
        -----------
        wave : ndarray
            Wavelength array
        flux : ndarray
            Flux array
        waveunits : :py:class:`~pysynphot.units.WaveUnits` object or subclass
            Units of wave
        fluxunits : :py:class:`~pysynphot.units.FluxUnits` object or subclass
            Units of flux
        name : string
            Description of this array
        keepneg :  bool [Default: False]
            If true, negative flux values will be retained; by default, they are forced to zero

        """
        if len(wave)!=len(flux):
            raise ValueError("wave and flux arrays must be of equal length")

        self._wavetable=wave
        self._fluxtable=flux
        self.waveunits=units.Units(waveunits)
        self.fluxunits=units.Units(fluxunits)
        self.name=name
        self.isAnalytic=False
        self.warnings={}

        self.validate_units() #must do before validate_fluxtable because it tests against unit type
        self.validate_wavetable() #must do before ToInternal in case of descending
        if not keepneg:
            self.validate_fluxtable()

        self.ToInternal()


class FileSourceSpectrum(TabularSourceSpectrum):
    """ Create a spectrum from a file.

    spec = FileSpectrum(filename (FITS or ASCII),
    fluxname=column name containing flux (for FITS tables only),
    keepneg=True to override thedefault behavior of setting negative
    flux values to zero)"""

    def __init__(self, filename, fluxname=None, keepneg=False):
        """
        Parameters
        -----------
        filename : string
            FITS or ASCII file containing the spectrum

        fluxname : string
            Column name specifying the flux (FITS only)

        keepneg : bool [Default: False]
            If true, negative flux values will be retained; by default, they are forced to zero

        """
        self.name = locations.irafconvert(filename)
        self._readSpectrumFile(self.name, fluxname)
        self.validate_units()
        self.validate_wavetable()
        if not keepneg:
            self.validate_fluxtable()
        self.ToInternal()
        self.isAnalytic=False
        self.warnings={}

    def _readSpectrumFile(self, filename, fluxname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, fluxname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, fluxname):
        fs = pyfits.open(filename)

        self._wavetable = fs[1].data.field('wavelength')
        if fluxname == None:
            fluxname = 'flux'
        self._fluxtable = fs[1].data.field(fluxname)
        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.fluxunits = units.Units(fs[1].header['tunit2'].lower())

        #Retain the header information as a convenience for the user.
        #If duplicate keywords exist, the value in the extension
        #header will override that in the primary.
        self.fheader = dict(fs[0].header)
        self.fheader.update(dict(fs[1].header))

        fs.close()

    def _readASCII(self, filename):
        """ Ascii files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is flux in Flam."""

        self.waveunits = units.Units('angstrom')
        self.fluxunits = units.Units('flam')
        wlist,flist = self._columnsFromASCII(filename)
        self._wavetable=np.array(wlist,dtype=np.float64)
        self._fluxtable=np.array(flist,dtype=np.float64)

        #We don't support headers from ascii files
        self.fheader = dict()


class AnalyticSpectrum(SourceSpectrum):
    ''' Base class for analytic functions. These are spectral forms
    which are defined, by default, on top of the default synphot
    waveset.
    '''

    def __init__(self,waveunits='angstrom',fluxunits='photlam'):
        "All AnalyticSpectra must set wave & flux units; do it here."
        self.waveunits = units.Units(waveunits)
        self.fluxunits = units.Units(fluxunits)
        self.validate_units()
        self.isAnalytic=True
        self.warnings={}

    def GetWaveSet(self):
        return refs._default_waveset.copy()


class GaussianSource(AnalyticSpectrum):
    """ Defines a gaussian source


    spec = GaussianSource(TotalFlux under Gaussian,
                             central wavelength of Gaussian,
                             FWHM of Gaussian,
                             waveunits, fluxunits)

    """
    def __init__(self, flux, center, fwhm, waveunits='angstrom',
                 fluxunits='flam'):
        """
        Parameters
        ----------
        flux : float
            TotalFlux under gaussian
        center : float
            central wavelength of gaussian
        fwhm : float
            full-width half-maximum (FWHM) of gaussian
        waveunits : string [Default: 'angstrom']
            units of input wavelengths
        fluxunits : string [Default: 'flam']
            units of input fluxes
        """
        AnalyticSpectrum.__init__(self,waveunits,fluxunits)

        self.center = center

        self.fwhm = fwhm

        self.total_flux = flux

        self._input_flux_units = self.fluxunits
        self._input_wave_units = self.waveunits

        self.sigma = fwhm / math.sqrt(8.0 * math.log(2.0))

        self.factor = flux / (math.sqrt(2.0 * math.pi) * self.sigma)

        self.name ='Gaussian: mu=%g %s,fwhm=%g %s, total flux=%g %s' % (self.center,
                                                                  self._input_wave_units,
                                                                  self.fwhm,
                                                                  self._input_wave_units,
                                                                  self.total_flux,
                                                                  self._input_flux_units)

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        # wavelength comes in as Angstom but Gaussian properties are stored
        # in user defined units
        wave = units.Angstrom().Convert(wavelength,self._input_wave_units.name)

        # calculate flux
        flux = self.factor * \
                np.exp(-0.5 * ((wave - self.center) / self.sigma)**2)

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        # convert flux to photlam before returning
        return self._input_flux_units.ToPhotlam(wave, flux, area=area)

    def GetWaveSet(self):
        '''Return a wavelength set that describes the Gaussian.
        Overrides the base class to compute 101 values, from
        center - 5*sigma to center + 5*sigma, in units of
        0.1*sigma
        '''
        increment = 0.1*self.sigma
        first = self.center - 50.0*increment
        last = self.center + 50.0*increment

        return np.arange(first, last, increment)


class FlatSpectrum(AnalyticSpectrum):
    """ Defines a flat spectrum in units of fluxunits.

    spec = FlatSpectrum(Flux density, waveunits, fluxunits).
    """
    def __init__(self, fluxdensity, waveunits='angstrom', fluxunits='photlam'):
        AnalyticSpectrum.__init__(self,waveunits,fluxunits)
        self.wavelength = None
        self._fluxdensity = fluxdensity
        self._input_flux_units = self.fluxunits
        self.name="Flat spectrum of %g %s"%(self._fluxdensity,
                                            self._input_flux_units)
    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        if hasattr(wavelength,'shape'):
            flux = self._fluxdensity * np.ones(wavelength.shape, dtype=np.float64)
        else:
            flux = self._fluxdensity

        # __call__ is supposed to return photflam so we need to do the
        # conversion here since it doesn't make sense to store the _fluxdensity
        # attribute in photlam
        wave = units.Angstrom().Convert(wavelength,self.waveunits.name)

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        return self._input_flux_units.ToPhotlam(wave, flux, area=area)


    def redshift(self, z):
        """Call the parent's method, which returns a TabularSourceSpectrum,
        then use its results to create a new FlatSpectrum with the correct
        value. """

        tmp=SourceSpectrum.redshift(self,z)
        ans=FlatSpectrum(tmp.flux.max(),
                         fluxunits=tmp.fluxunits)
        return ans

##This change produces 5 errors and 17 failures in cos_etc_test.py
##     def GetWaveSet(self):
##         return np.array([_default_waveset[0],_default_waveset[-1]])


class Powerlaw(AnalyticSpectrum):
    """ Defines a power law spectrum

    spec=PowerLaw(refwave, exponent, waveunits, fluxunits).

    Power law spectrum of the form (lambda/refval)**exponent,
    where refval is in Angstroms.
    The spectrum is normalized to a flux of 1 in "fluxunits" at "refval".
    """
    def __init__(self, refwave, index, waveunits='angstrom', fluxunits='photlam'):
        AnalyticSpectrum.__init__(self,waveunits,fluxunits)
        self.wavelength = None

        self._input_flux_units = self.fluxunits
        self._input_wave_units = self.waveunits

        self._refwave = refwave

        self._index = index

        self.name="Power law: refwave %g %s, index %g"%(self._refwave,self._input_wave_units,self._index)

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        # input wavelength is assumed to be angstroms
        # and either a scalar or a numpy array

        # need to first convert input wavelength to the units the user
        # specified when creating this object
        wave = units.Angstrom().Convert(wavelength,self._input_wave_units.name)

        flux = (wave / self._refwave) ** self._index

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = None

        # convert flux to photlam before returning
        return self._input_flux_units.ToPhotlam(wave, flux, area=area)


class BlackBody(AnalyticSpectrum):
    """     Blackbody spectrum with specified temperature, in Kelvin.

    spec = BlackBody(T in Kelvin)

    The flux of the spectrum is normalized to a star of solar radius
    at a distance of 1 kpc.L
    """
    def __init__(self, temperature):
        waveunits=units.Units('angstrom')
        fluxunits=units.Units('photlam')
        AnalyticSpectrum.__init__(self,waveunits,fluxunits)
        self.wavelength = None
        self.temperature = temperature
        self.name='BB(T=%d)'%self.temperature

    def __str__(self):
        return self.name

    def __call__(self, wavelength):
        return planck.bbfunc(wavelength, self.temperature) * RENORM


class SpectralElement(Integrator):
    '''Base class for a Spectral Element (e.g. Filter, Detector...).
    '''
    def __init__(self):
        self.binset = None

    def validate_units(self):
        "Ensure that waveunits are WaveUnits"
        if (not isinstance(self.waveunits,units.WaveUnits)):
            raise TypeError("%s is not a valid WaveUnit"%self.waveunits)

    def __mul__(self, other):
        '''Permitted to multiply a SpectralElement by another
        SpectralElement, or by a SourceSpectrum.  In the former
        case we return a CompositeSpectralElement, while in the
        latter case a CompositeSourceSpectrum.
        '''
        if isinstance(other, SpectralElement):
            return CompositeSpectralElement(self, other)

        if isinstance(other, SourceSpectrum):
            return CompositeSourceSpectrum(self, other, 'multiply')

        ## Multiplying by a constant is the same as multiplying by a
        ## UniformTransmission object
        if isinstance(other, (int, float)):
            return CompositeSpectralElement(self, UniformTransmission(other))

        else:
            print "SpectralElements can only be multiplied by other " + \
                  "SpectralElements or SourceSpectrum objects"

    def __rmul__(self, other):
        return self.__mul__(other)


    def integrate(self,wave=None):
        """Integrate the throughput over the specified waveset,
        if None, integrate over the full waveset."""
        if  wave is None:
            wave=self.wave
        ans=self.trapezoidIntegration(wave,self(wave))
        return ans

#..................................................................
# Methods to implement bandpar functionality go here
#..................................................................
    def avgwave(self):
        """Implement the equation for lambda nought as defined
        in Koornneef et al 1987, p 836.
        Should be equivalent to bandpar.avglam = bandpar.avgwv"""

        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave=self.wave
        thru=self.throughput
        self.convert(mywaveunits)

        num = self.trapezoidIntegration(wave, thru*wave)
        den = self.trapezoidIntegration(wave, thru)


        if 0.0 in (num, den):
            return 0.0
        else:
            return num/den

    def pivot(self,binned=False):
        """This is the calculation performed when the ETC invokes calcphot.
        Does this need to be calculated on binned waveset, or may
        it be calculated on native waveset?"""
        if binned:
            try:
              wave = self.binwave
            except AttributeError:
              raise AttributeError('Class ' + str(type(self)) + ' does not support binning.')
        else:
            wave = self.wave

        countmulwave = self(wave)*wave
        countdivwave = self(wave)/wave

        num = self.trapezoidIntegration(wave,countmulwave)
        den = self.trapezoidIntegration(wave,countdivwave)

        if num == 0.0 or den == 0.0:
            return 0.0

        return math.sqrt(num/den)

    def rmswidth(self, floor=0):
        """
        Calculate the RMS width as in Koornneef et al 1987, p 836.

        Parameters
        ----------
        floor : float, optional
            Points with throughputs below this threshold are not
            included in the calculation. By default all points
            are included.

        Returns
        -------
        rmswidth : float
            RMS width of the bandpass.

        """

        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave=self.wave
        thru=self.throughput
        self.convert(mywaveunits)

        if floor != 0:
            idx = np.where(thru >= floor)
            wave = wave[idx]
            thru = thru[idx]

        integrand = (wave-self.avgwave())**2 * thru
        num = self.trapezoidIntegration(wave, integrand)
        den = self.trapezoidIntegration(wave, thru)

        if 0.0 in (num, den):
            return 0.0
        else:
            ans = math.sqrt(num/den)
            return ans

    def photbw(self, floor=0):
        """
        This is a compatibility function allowing pysynphot to calculate
        the bandpass RMS width in the same way as Synphot (documented
        in the Synphot Manual section 5.1). This is the value returned
        in the BANDW keyword by Synphot's bandpar function.

        This function is designed only for use to get the same results
        as Synphot. To calculate the bandpass RMS width use the
        `rmswidth` method.

        Parameters
        ----------
        floor : float, optional
            Points with throughputs below this threshold are not
            included in the calculation. By default all points
            are included.

        Returns
        -------
        photbw : float
            RMS width of the bandpass.

        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave=self.wave
        thru=self.throughput
        self.convert(mywaveunits)

        # calculate the average wavelength
        num = self.trapezoidIntegration(wave, thru * np.log(wave) / wave)
        den = self.trapezoidIntegration(wave, thru / wave)

        if num == 0 or den == 0:
            error_str = 'Could not calculate average wavelength of bandpass.'
            raise exceptions.PysnphotErorr(error_str)

        avg_wave = np.exp(num/den)

        if floor != 0:
            idx = np.where(thru >= floor)
            wave = wave[idx]
            thru = thru[idx]

        # calcualte the rms width
        integrand = thru * np.log(wave / avg_wave)**2 / wave
        num = self.trapezoidIntegration(wave, integrand)

        if num == 0 or den == 0:
            return 0.0

        return avg_wave * np.sqrt(num/den)

    def rectwidth(self):
        """RECTW = INT(THRU) / MAX(THRU)"""
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave=self.wave
        thru=self.throughput
        self.convert(mywaveunits)

        num = self.trapezoidIntegration(wave, thru)
        den = thru.max()

        if 0.0 in (num, den):
            return 0.0
        else:
            return num/den

    def equivwidth(self):
        """ EQUVW = INT(THRU)        """

        return self.integrate()

    def efficiency(self):
        """QTLAM = dimensionless efficience
                 = INT(THRU / LAM)
        """
        mywaveunits = self.waveunits.name
        self.convert('angstroms')

        wave=self.wave
        thru=self.throughput
        self.convert(mywaveunits)

        ans = self.trapezoidIntegration(wave, thru/wave)
        return ans

#..................................................................
    def check_sig(self, other):
        """Only call this if check_overlap returns 'partial'.
        Returns True if the LACK of overlap is INsignificant:
        i.e., it is ok to go ahead and do whatever we are doing."""

        swave=self.wave[np.where(self.throughput != 0)]
        s1,s2=swave.min(),swave.max()

        owave=other.wave
        o1,o2=owave.min(),owave.max()

        lorange=sorted([s1,o1])
        hirange=sorted([s2,o2])

        #Get the full throughput
        total=self.integrate()

        #Now get the other two pieces
        #We cannot yet do
        #low=self[slice(*lowrange)].integrate()
        wave=self.wave
        idxs=[np.searchsorted(wave, lorange, 'left'),
              np.searchsorted(wave, hirange, 'left')]

        excluded=0.0
        for idx in idxs:
            try:
                excluded+=self.integrate(wave=wave[slice(*idx)])
            except IndexError:
                pass #If the range is zero, do nothing

        if excluded/total < 0.01:
            return True
        else:
            return False

    def check_overlap(self, other):
        """Check whether the wavelength range of other is defined everywhere
        that the wavelength range of self is defined.
        Returns "full", "partial", "none".
        Normally used for checking whether a spectrum is fully defined over
        the range of a bandpass.
        Note that the full overlap case is asymmetric: if the range of 'self'
        extends past the limits of 'other', this will return a partial
        overlap.
        """

        if other.isAnalytic:
            #then it's defined everywhere
            return 'full'

        swave=self.wave[np.where(self.throughput != 0)]
        s1,s2=swave.min(),swave.max()

        owave=other.wave
        o1,o2=owave.min(),owave.max()

        if (s1>=o1 and s2<=o2):
            ans='full'

        elif (s2<o1) or (o2<s1):
            ans='none'

        else:
            ans='partial'

        return ans

    def convert(self, targetunits):
        '''Convert to other units. This method actually just changes the
        wavelength unit objects, it does not recompute the
        internally kept wave data; these are kept always in internal
        units. Method getWaveSet does the actual computation.'''
        nunits = units.Units(targetunits)
        self.waveunits = nunits


    def ToInternal(self):
        '''Convert wavelengths to the internal representation of angstroms..
        Note: This is not yet used, but should be for safety when creating
        TabularSpectralElements from files. It will also be necessary for the
        ArraySpectralElement class that we want to create RSN.
        '''
        self.validate_units()
        savewunits = self.waveunits
        angwave = self.waveunits.Convert(self.GetWaveSet(), 'angstrom')
        self._wavetable = angwave.copy()
        self.waveunits = savewunits


    def __call__(self, wavelengths):
        '''This is where the throughput array is calculated for a given
        input wavelength table.
        wavelengths : ndarray
            an array of wavelengths in Angstroms at which the
                             throughput should be sampled
        '''
        if np.isscalar(wavelengths):
            delta=0.0001
            ww=np.array([wavelengths-delta,wavelengths,wavelengths+delta])
            tmp=self.resample(ww)
            return tmp._throughputtable[1]
        else:
            return self.resample(wavelengths)._throughputtable

    def sample(self, wave):
        """Provide a more normal user interface to the __call__"""
        angwave = self.waveunits.ToAngstrom(wave)

        return self.__call__(angwave)


    def taper(self):
        '''Taper the spectrum by adding zeros to each end.
        '''
        OutElement = TabularSpectralElement()

        wcopy = np.zeros(self._wavetable.size+2,dtype=np.float64)
        fcopy = np.zeros(self._throughputtable.size+2,dtype=np.float64)

        wcopy[1:-1] = self._wavetable
        fcopy[1:-1] = self._throughputtable

        fcopy[0] = 0.0
        fcopy[-1] = 0.0

        ## The wavelengths to use for the first and last points are
        ## calculated by using the same ratio as for the 2 interior points
        wcopy[0] = wcopy[1]*wcopy[1]/wcopy[2]
        wcopy[-1] = wcopy[-2]*wcopy[-2]/wcopy[-3]

        OutElement._wavetable = wcopy
        OutElement._throughputtable = fcopy

        return OutElement

    def writefits(self, filename, clobber=True, trimzero=True,
                  precision=None, hkeys=None):
        """Write the bandpass to a FITS file.

        Parameters
        -----------
        filename : string
            name of file to write to
        clobber : bool [Default: True]
            Will clobber existing file by default
        trimzero : bool [Default: True]
            Will trim zero-flux elements from both ends by default
        precision : {'single','double',None}
            Will write in native precision by default
        hkeys : dict, optional
            Optional dictionary of {keyword:(value,comment)}
                   to be added to primary FITS header

        """
        if precision is None:
            precision=self.throughput.dtype.char
        _precision=precision.lower()[0]
        pcodes={'d':'D','s':'E','f':'E'}

        if clobber:
            try:
                os.remove(filename)
            except OSError:
                pass

        wave=self.wave
        thru=self.throughput

        #Add a check for single/double precision clash, so
        #that if written out in single precision, the wavelength table
        #will still be sorted with no duplicates
        #The value of epsilon is taken from the Synphot FAQ.

        if wave.dtype == np.float64 and _precision == 's':
            idx=np.where(abs(wave[1:]-wave[:-1]) > syn_epsilon)
        else:
            idx=np.where(wave) #=> idx=[:]

        wave=wave[idx]
        thru=thru[idx]


        first,last=0,len(thru)
        if trimzero:
            #Keep one zero at each end
            nz = thru.nonzero()[0]
            try:
                first=max(nz[0]-1,first)
                last=min(nz[-1]+2,last)
            except IndexError:
                pass

        #Construct the columns and HDUlist
        cw = pyfits.Column(name='WAVELENGTH',
                           array=wave[first:last],
                           unit=self.waveunits.name,
                           format=pcodes[_precision])
        cf = pyfits.Column(name='THROUGHPUT',
                           array=thru[first:last],
                           unit='         ',
                           format=pcodes[_precision])

        #Make the primary header
        hdu = pyfits.PrimaryHDU()
        hdulist = pyfits.HDUList([hdu])


        #User-provided keys are written to the primary header;
        #so are filename and origin
        bkeys = dict(filename=(os.path.basename(filename),'name of file'),
                     origin=('pysynphot',
                             'Version (%s, %s)'%(__version__,__svn_revision__)))
        #User-values if present may override default values
        if hkeys is not None:
            bkeys.update(hkeys)

        #Now update the primary header
        for key,val in bkeys.items():
            hdu.header.update(key, *val)


        #Make the extension HDU
        cols = pyfits.ColDefs([cw, cf])
        hdu = pyfits.new_table(cols)

        #There are also some keys to be written to the extension
        #header

        bkeys=dict(expr  =(str(self),'pysyn expression'),
                   tdisp1=('G15.7',),
                   tdisp2=('G15.7',)
                   )

        try:
            bkeys['grftable']=(os.path.basename(self.obsmode.gtname),
                               'graph table used')
            bkeys['cmptable']=(os.path.basename(self.obsmode.ctname),
                               'component table used')
        except AttributeError:
            pass #Not all bandpasses have these

        for key,val in bkeys.items():
            hdu.header.update(key, *val)

        #Add the extension to the list, and write to file.
        hdulist.append(hdu)
        hdulist.writeto(filename)



    def resample(self, resampledWaveTab):
        '''Interpolate throughput given a wavelength array that is
        monotonically increasing and the TabularSpectralElement object.'''
        ##Check whether the input wavetab is in descending order

        if resampledWaveTab[0]<resampledWaveTab[-1]:
            newwave=resampledWaveTab
            newasc = True
        else:
            newwave=resampledWaveTab[::-1]
            newasc = False

        ## Use numpy interpolation function
        if self._wavetable[0]<self._wavetable[-1]:
            oldasc = True
            ans = np.interp(newwave,self._wavetable,
                           self._throughputtable)
        else:
            oldasc = False
            rev = np.interp(newwave,self._wavetable[::-1],
                           self._throughputtable[::-1])
            ans = rev[::-1]

        ## If the new and old waveset don't have the same parity,
        ## the answer has to be flipped again
        if (newasc != oldasc):
            ans=ans[::-1]

        # Finally, make the new object.
        # NB: these manipulations were done using the internal
        #tables in Angstrom, so those are the units
        #that must be fed to the constructor.
        resampled=ArraySpectralElement(wave=resampledWaveTab.copy(),
                                       waveunits = 'angstroms',
                                       throughput = ans.copy())
        #Use the convert method to set the units desired by the user.
        resampled.convert(self.waveunits)

        return resampled

    def unit_response(self):
        """
        Returns flux, in flam, of a star that produces a response of
        one photon per second in this passband.

        Only correct if waveunits are Angstrom.

        """
        hc = units.HC

        if hasattr(self, 'primary_area'):
            area = self.primary_area
        else:
            area = refs.PRIMARY_AREA

        wave = self.GetWaveSet()
        thru = self(wave)

        return hc / (area * self.trapezoidIntegration(wave, thru*wave))


    def GetWaveSet(self):
        "Return the waveset in the requested units."
        wave = units.Angstrom().Convert(self._wavetable, self.waveunits.name)
        return wave

    def GetThroughput(self):
        """Return the throughput for the internal wavetable."""
        ## NB: Throughput never changes units no matter what the
        ## wavelength does. There is an implicit assumption here that
        ## the units of the input waveset to the __call__ are always
        ## Angstroms.
        self.convert('angstroms')
        return self.__call__(self.wave)

    wave = property(GetWaveSet, doc='Waveset for bandpass')
    throughput = property(GetThroughput, doc='Throughput for bandpass')

    def fwhm(self):
        raise NotImplementedError("#139: Implement calcband functionality")


class CompositeSpectralElement(SpectralElement):
    '''CompositeSpectralElement Class, which knows how to calculate
    its throughput by delegating the calculating the calculating to
    its components.
    '''
    def __init__(self, component1, component2):
        SpectralElement.__init__(self)

        if (not isinstance(component1, SpectralElement) or
            not isinstance(component2, SpectralElement)):
            raise TypeError("Arguments must be SpectralElements")

        self.component1 = component1
        self.component2 = component2

        self.isAnalytic = component1.isAnalytic and component2.isAnalytic

        if component1.waveunits.name == component2.waveunits.name:
            self.waveunits = component1.waveunits
        else:
            msg="Components have different waveunits (%s and %s)"%(component1.waveunits,component2.waveunits)
            raise NotImplementedError(msg)

        self.throughputunits = None

        self.name="(%s * %s)"%(str(self.component1),str(self.component2))

        self.warnings={}
        self.warnings.update(component1.warnings)
        self.warnings.update(component2.warnings)

         # check areas
        if hasattr(component1, 'primary_area'):
            comp1_area = component1.primary_area
        else:
            comp1_area = None

        if hasattr(component2, 'primary_area'):
            comp2_area = component2.primary_area
        else:
            comp2_area = None

        if not comp1_area and not comp2_area:
            self.primary_area = None

        elif comp1_area and not comp2_area:
            self.primary_area = comp1_area

        elif not comp1_area and comp2_area:
            self.primary_area = comp2_area

        else:
            if comp1_area == comp2_area:
                self.primary_area = comp1_area

            else:
                err = 'Components have different area attributes: %s: %f, %s: %f'
                err = err % (str(component1), comp1_area,
                             str(component2), comp2_area)
                raise exceptions.IncompatibleSources(err)

    def __call__(self, wavelength):
        '''This is where the throughput calculation is delegated.
        '''
        return self.component1(wavelength) * self.component2(wavelength)

    def __str__(self):
        return self.name

    def complist(self):
        ans=[]
        for comp in (self.component1, self.component2):
            try:
                ans.extend(comp.complist())
            except AttributeError:
                ans.append(comp)
        return ans

    def GetWaveSet(self):
        '''This method returns a wavelength set appropriate for a composite
        object by forming the union of the wavelengths of the components.
        '''
        wave1 = self.component1.GetWaveSet()
        wave2 = self.component2.GetWaveSet()

        return MergeWaveSets(wave1, wave2)

    wave = property(GetWaveSet,doc="wave for CompositeSpectralElement")


class UniformTransmission(SpectralElement):
    '''bandpass=UniformTransmission(dimensionless throughput)

    .. todo::

        Need to add a GetWaveSet method (or just return None).

    '''
    def __init__(self, value, waveunits='angstrom'):
        SpectralElement.__init__(self)

        self.waveunits = units.Units(waveunits)
        self.value = value
        self.name=str(self)
        self.isAnalytic=True
        self.warnings={}
        #The ._wavetable is used only by the .writefits() method at this time
        #It is not for general use.
        self._wavetable = np.array([refs._default_waveset[0],refs._default_waveset[-1]])

    def __str__(self):
        return "%g"%self.value

    def GetWaveSet(self):
        return None

    def check_overlap(self, spectrum):
        """ Apply special overlap logic for UniformTransmission.

        By definition, a UniformTransmission is defined everywhere.
        Therefore, this is a special case for which the overlap check
        should be ignored (because the alternative is that it will
        always fail and always require users to override it, so it
        becomes meaningless).

        """
        pass


## This produced 15 test failures in cos_etc_test.
##     def GetWaveSet(self):
##         return np.array([_default_waveset[0],_default_waveset[-1]])
##
##     wave = property(GetWaveSet,doc="wave for UniformTransmission")

    def __call__(self, wavelength):
        '''__call__ returns the constant value as an array, given a
        wavelength array as argument.
        '''
        return 0.0 * wavelength + self.value


class TabularSpectralElement(SpectralElement):
    """bandpass = FileBandpass(FITS or ASCII filename, thrucol= name of
    column containing throughput values (for FITS tables only)
    """
    def __init__(self, fileName=None, thrucol='throughput'):
        '''__init__ takes a character string argument that contains the name
        of the file with the spectral element table.
        '''
        SpectralElement.__init__(self)

        self.isAnalytic=False
        self.warnings={}
        if fileName:
            if fileName.endswith('.fits') or fileName.endswith('.fit'):
                self._readFITS(fileName, thrucol)
            else:
                self._readASCII(fileName)
            self.name = fileName

        else:
            self.name = None
            self._wavetable = None
            self._throughputtable = None
            self.waveunits = None
            self.throughputunits = None

    def _reverse_wave(self):
        self._wavetable = self._wavetable[::-1]

    def __str__(self):
        return str(self.name)

    def ToInternal(self):
        '''Convert wavelengths to the internal representation of angstroms..
        '''
        self.validate_units()
        savewunits = self.waveunits
        angwave = self.waveunits.Convert(self._wavetable, 'angstrom')
        self._wavetable = angwave.copy()
        self.waveunits = savewunits


    def _readASCII(self,filename):
        """ Ascii files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is throughput (dimensionless)."""
        self.waveunits = units.Units('angstrom')
        self.throughputunits = 'none'
        wlist,tlist = self._columnsFromASCII(filename)
        self._wavetable=np.array(wlist,dtype=np.float64)
        self._throughputtable=np.array(tlist,dtype=np.float64)


    def _readFITS(self,filename,thrucol='throughput'):
        fs = pyfits.open(filename)

        self._wavetable = fs[1].data.field('wavelength')
        self._throughputtable = fs[1].data.field(thrucol)

        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.throughputunits = 'none'

        self.getHeaderKeywords(fs[1].header)

        fs.close()


    def getHeaderKeywords(self, header):
        ''' This is a placeholder for subclasses to get header keywords without
        having to reopen the file again.
        '''
        pass


class ArraySpectralElement(TabularSpectralElement):
    """ spec = ArraySpectrum(numpy array containing wavelength table,
    numpy array containing throughput table, waveunits,
    name=human-readable nickname for bandpass.
    """
    def __init__(self, wave=None, throughput=None,
                 waveunits='angstrom',
                 name='UnnamedArrayBandpass'):

        """Create a spectrum from arrays.

        Parameters
        ----------
        wave : ndarray
            Wavelength array
        throughput : ndarray
            Throughput array
        waveunits : :py:class:`~pysynphot.units.WaveUnits` object or subclass
            Units of wave
        name : string
            Description of this spectral element

        """
        if len(wave) != len(throughput):
            raise ValueError("wave and throughput arrays must be of equal length")

        self._wavetable=wave
        self._throughputtable=throughput
        self.waveunits=units.Units(waveunits)
        self.name=name
        self.isAnalytic=False
        self.warnings={}

        self.validate_units() #must do before validate_fluxtable because it tests against unit type
        self.validate_wavetable() #must do before ToInternal in case of descending

        self.ToInternal()


class FileSpectralElement(TabularSpectralElement):
    """ Create a bandpass from a file.

    spec = FileSpectrum(filename (FITS or ASCII),
    throughputname=column name containing throughput (for FITS tables only),
    keepneg=True to override the default behavior of setting negative
    throughput values to zero)"""

    def __init__(self, filename, thrucol=None):
        """

        Parameters
        -----------
        filename : string
            FITS or ASCII file containing the bandpass
        thrucol : string
            Column name specifying the throughput (FITS only)

        """
        self.name = locations.irafconvert(filename)
        self._readThroughputFile(self.name, thrucol)

        self.validate_units()
        self.validate_wavetable()
        self.ToInternal()
        self.isAnalytic=False
        self.warnings={}

    def _readThroughputFile(self, filename, throughputname):
        if filename.endswith('.fits') or filename.endswith('.fit'):
            self._readFITS(filename, throughputname)
        else:
            self._readASCII(filename)

    def _readFITS(self, filename, throughputname):
        fs = pyfits.open(filename)

        self._wavetable = fs[1].data.field('wavelength')
        if throughputname == None:
            throughputname = 'throughput'
        self._throughputtable = fs[1].data.field(throughputname)
        self.waveunits = units.Units(fs[1].header['tunit1'].lower())

        #Retain the header information as a convenience for the user.
        #If duplicate keywords exist, the value in the extension
        #header will override that in the primary.
        self.fheader = dict(fs[0].header)
        self.fheader.update(dict(fs[1].header))

        fs.close()

    def _readASCII(self, filename):
        """ Ascii files have no headers. Following synphot, this
        routine will assume the first column is wavelength in Angstroms,
        and the second column is throughput in Flam."""

        self.waveunits = units.Units('angstrom')
        wlist,flist = self._columnsFromASCII(filename)
        self._wavetable=np.array(wlist,dtype=np.float64)
        self._throughputtable=np.array(flist,dtype=np.float64)

        #We don't support headers from asii files
        self.fheader = dict()

class InterpolatedSpectralElement(SpectralElement):
    '''The InterpolatedSpectralElement class handles spectral elements
    that are interpolated from columns stored in FITS tables
    '''
    def __init__(self, fileName, wavelength):
        ''' The file name contains a suffix with a column name specification
        in between square brackets, such as [fr388n#]. The wavelength
        parameter (poorly named -- it is not always a wavelength) is used to
        interpolate between two columns in the file.
        '''
        SpectralElement.__init__(self)

        xre=re.search('\[(?P<col>.*?)\]',fileName)
        self.name = os.path.expandvars(fileName[0:(xre.start())])
        colSpec = xre.group('col')

        self.analytic=False
        self.warnings={}

        self.interpval = wavelength

        fs = pyfits.open(self.name)

        # if the file has the PARAMS header keyword and if it is set to
        # WAVELENGTH then we want to perform a wavelength shift before
        # interpolation, otherwise we don't want to shift.
        if 'PARAMS' in fs[0].header and fs[0].header['PARAMS'].lower() == 'wavelength':
            doshift = True
        else:
            doshift = False

        # check whether we are supposed to extrapolate when we're given an
        # interpolation value beyond the columns of the table.
        # extrapolation is assumed to false if the EXTRAP keyword is missing.
        if 'EXTRAP' in fs[0].header and fs[0].header['EXTRAP'] is True:
            extrapolate = True
        else:
            extrapolate = False

        #The wavelength table will have to be adjusted before use
        wave0 = fs[1].data.field('wavelength')


        #Determine the columns that bracket the desired value
        # grab all columns that beging with the parameter name (e.g. 'MJD#')
        # then split off the numbers after the '#'
        colNames = [n for n in fs[1].data.names if n.startswith(colSpec.upper())]
        colWaves = [float(cn.split('#')[1]) for cn in colNames]

        if colNames == []:
            raise StandardError('File %s contains no interpolated columns.' % (fileName,))

        # easy case: wavelength matches a column
        if self.interpval in colWaves:
            self._no_interp_init(wave0, fs[1].data[colNames[colWaves.index(wavelength)]])

        # need interpolation
        elif self.interpval > colWaves[0] and self.interpval < colWaves[-1]:
            upper_ind = np.searchsorted(colWaves,self.interpval)
            lower_ind = upper_ind - 1

            self._interp_init(wave0,colWaves[lower_ind],colWaves[upper_ind],
                              fs[1].data[colNames[lower_ind]],
                              fs[1].data[colNames[upper_ind]],doshift)

        # extrapolate below lowest columns
        elif extrapolate and self.interpval < colWaves[0]:
            self._extrap_init(wave0,colWaves[0],colWaves[1],
                              fs[1].data[colNames[0]],
                              fs[1].data[colNames[1]])

        # extrapolate above highest columns
        elif extrapolate and self.interpval > colWaves[-1]:
            self._extrap_init(wave0,colWaves[-2],colWaves[-1],
                              fs[1].data[colNames[-2]],
                              fs[1].data[colNames[-1]])

        # can't extrapolate, use default
        elif not extrapolate and 'THROUGHPUT' in fs[1].data.names:
            s = 'Extrapolation not allowed, using default throughput for %s' % (fileName,)
            warnings.warn(s,UserWarning)
            self.warnings['DefaultThroughput'] = True
            self._no_interp_init(wave0,fs[1].data['THROUGHPUT'])

        # can't extrapolate and no default
        elif not extrapolate and 'THROUGHPUT' not in fs[1].data.names:
            s = 'Cannot extrapolate and no default throughput for %s' % (fileName,)
            raise exceptions.ExtrapolationNotAllowed(s)

        # assign units
        self.waveunits = units.Units(fs[1].header['tunit1'].lower())
        self.throughputunits = 'none'

        fs.close()

    def __str__(self):
        return "%s#%g"%(self.name,self.interpval)

    def _no_interp_init(self,waves,throughput):
        self._wavetable = waves
        self._throughputtable = throughput

    def _interp_init(self,waves,lower_val,upper_val,lower_thru,upper_thru,doshift):
        self._wavetable = waves

        if doshift:
            #Adjust the wavelength table to bracket the range
            lwave = waves + (lower_val - self.interpval)
            uwave = waves + (upper_val - self.interpval)

            #Interpolate the columns at those ranges
            lower_thru = np.interp(lwave, waves, lower_thru)
            upper_thru = np.interp(uwave, waves, upper_thru)

        #Then interpolate between the two columns
        w = (self.interpval - lower_val) / (upper_val - lower_val)
        self._throughputtable = (upper_thru * w) + lower_thru * (1.0 - w)

    def _extrap_init(self,waves,lower_val,upper_val,lower_thru,upper_thru):
        self._wavetable = waves

        throughput = []

        for y1,y2 in zip(lower_thru,upper_thru):
            m = (y2 - y1) / (upper_val - lower_val)
            b = y1 - m * lower_val

            throughput.append(m*self.interpval + b)

        self._throughputtable = np.array(throughput)


class ThermalSpectralElement(TabularSpectralElement):
    '''The ThermalSpectralElement class handles spectral elements
    that have associated thermal properties read from a FITS table.

    ThermalSpectralElements differ from regular SpectralElements in
    that they carry thermal parameters such as temperature and beam
    filling factor, but otherwise they operate just as regular
    SpectralElements. They dont know how to apply themselves to an
    existing beam, in the sense that their emissivities should be
    handled explictly, outside the objects themselves.
    '''
    def __init__(self, fileName):

        TabularSpectralElement.__init__(self, fileName=fileName, thrucol='emissivity')
        self.warnings={}

    def getHeaderKeywords(self, header):
        ''' Overrides base class in order to get thermal keywords.
        '''
        self.temperature = header['DEFT']
        self.beamFillFactor = header['BEAMFILL']


class Box(SpectralElement):
    """bandpass = Box(central wavelength, width) - both in Angstroms"""
    def __init__(self, center, width, waveunits=None):
        ''' Both center and width are assumed to be in Angstrom
            units, according to the synphot definition.
        '''
        SpectralElement.__init__(self)

        if waveunits is None:
            self.waveunits=units.Units('angstrom') #per docstring: for now
        else:
            self.waveunits=units.Units(waveunits)
            center = self.waveunits.Convert(center, 'angstrom')
            width  = self.waveunits.Convert(width, 'angstrom')

        lower = center - width / 2.0
        upper = center + width / 2.0
        step = 0.05                     # fixed step for now (in A)

        self.name='Box at %g (%g wide)' % (center,width)
        nwaves = int(((upper - lower) / step)) + 2
        self._wavetable = np.zeros(shape=[nwaves,], dtype=np.float64)

        for i in range(nwaves):
            self._wavetable[i] = lower + step * i

        self._wavetable[0]  = self._wavetable[1]  - step
        self._wavetable[-1] = self._wavetable[-2] + step

        self._throughputtable = np.ones(shape=self._wavetable.shape, \
                                        dtype=np.float64)
        self._throughputtable[0]  = 0.0
        self._throughputtable[-1] = 0.0

        self.isAnalytic=False
        self.warnings={}

Vega = FileSourceSpectrum(locations.VegaFile)
