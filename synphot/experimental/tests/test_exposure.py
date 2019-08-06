from synphot.models import BlackBody1D
from synphot.spectrum import SourceSpectrum, SpectralElement
from synphot.experimental.exposure import Exposure
import astropy.units as u
import numpy as np


class TestExposure(object):
    """ Tests that each possible bandpass input returns a
    SpectralElement object """
    def setup_class(self):
        self.source_spec = SourceSpectrum(BlackBody1D, temperature=6000 * u.K)
        self.diameter = 1 * u.m
        self.exptime = 1 * u.s
        test_waves = np.arange(300, 1000) * u.nm
        test_trans = np.linspace(0, 1, len(test_waves)) * u.Unit('')
        self.test_throughput_list = [test_waves, test_trans]

    def test_bandpass_str(self):
        bp = 'johnson_u'
        result = Exposure(self.source_spec, self.diameter, self.exptime,
                          bandpass=bp).bandpass
        assert type(result) == SpectralElement

    def test_bandpass_list(self):
        result = Exposure(self.source_spec, self.diameter, self.exptime,
                          bandpass=self.test_throughput_list).bandpass
        assert type(result) == SpectralElement

        bp_flipped = [self.test_throughput_list[1],
                      self.test_throughput_list[0]]
        result_flipped = Exposure(self.source_spec, self.diameter,
                                  self.exptime, bandpass=bp_flipped).bandpass
        assert type(result_flipped) == SpectralElement

    def test_qe(self):
        result = Exposure(self.source_spec, self.diameter, self.exptime,
                          quantum_efficiency=self.test_throughput_list
                          ).quantum_efficiency

        assert type(result) == SpectralElement

    def test_atmosphere(self):
        result = Exposure(self.source_spec, self.diameter, self.exptime,
                          atmospheric_transmission=self.test_throughput_list
                          ).atmospheric_transmission

        assert type(result) == SpectralElement

    def test_snr(self):
        """ unfinished """
        result = Exposure(self.source_spec, self.diameter, self.exptime,
                          force='extrap').snr
        return result
