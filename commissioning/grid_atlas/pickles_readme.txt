A STELLAR SPECTRAL FLUX LIBRARY BY A.J. PICKLES (1998)
(PASP 110, 863)

This library of wide spectral coverage, consists of 131 flux calibrated
stellar spectra, encompassing all normal spectral types and luminosity
classes at solar abundance, and metal-weak and metal-rich F-K dwarf
and G-K giant components. Each spectrum in the library is a combination of
several sources overlapping in wavelength coverage. The creator of the 
library has followed precise criteria to combine sources and to assemble 
the most reliable spectra. As part of the selection criteria prior to 
combination, all  input sources were checked aginst the SIMBAD database 
and against the colors and line strengths as derived by the observed 
spectra themselves to make sure they had similar spectral types.

In the following, the list of the above mentioned input sources is given,
numbered following Table 1 in the original paper. 

1) Sviderskiene (1988)
2) Heck et al. (1984)
3) Gunn and Stryker (1983)
4) Kiehling (1987)
5) Jacobi, Hunter and Christian (1984)
6) Silva and Cornell (1992)
7) Pickles (1985)
8) Pickles and van der Kruit (1990)
9) Serote Roos, Boisson and Joly (1996)
10) Danks and Dennefeld (1994)
11) Lancon and Rocca-Volmerange (1992)
12) Dallier, Boisson and Joly (1996)
13) Kleinmann and Hall (1986)
14) Cohen et al. (1995, 1996a, 1996b)
15) Fluks et al. (1994)

Table 1 of Pickles (1998) precisely identifies what of the above sources
entered the combination to create the complete set of spectral types.
The output wavelength grid was chosen to be 1150-25000 Angstrom,
with a sampling interval of 5 Angstrom per pixel and resolution of
~500 Angstrom. In the end, two separate libraries were created, UVILIB and
UVKLIB, that cover the spectral range 1150-10620 Angstrom, and 1150-25000
Angstrom, respectively. In fact, only half of all spectral types in the
library (mainly later types of solar abundance) have longer spectral coverages
available.

The following quick-look table gives an idea of the spectra available.
Spectra are ordered by progressive number, according to the spectral type
(decreasing effective temperature) and luminosity class. The same ordering 
sequence is valid for both the UVILIB and the UVKLIB libraries, where the suffix 
"uk" differentiates between two spectra of the same spectral type but with 
different wavelength coverage (see ahead the section on the CDBS/HST Pickles 
library).



                      Table 1: Pickles library spectra:

                spectrum id no.        spectral types
                                     and luminosity class

                    1-45                 O5-M6 V
                   46-59                 B2-K3 IV
                   60-105                O8-M10 III
                  106-113                B2-M3 II
                  114-131                B0-M2 I


Some reasons why it is worth to use this library may be summarized as follows:

1) it provides an uniform and complete flux library of observed spectra
representing normal stellar types, and 

2) each spectrum was put together after selecting the best spectra in each
wavelength interval, grouping them by spectral type, luminosity class and
abundance (and color and line strength), to produce a final product with
an uniform grid.


THE HST/CDBS VERSION OF THE PICKLES LIBRARY

The library installed in CDBS and distributed within STSDAS is from
http://cdsarc.u-strasbg.fr/viz-bin/ftp-index?J/PASP/110/863.
This library  is divided in 2 independent subdirectories, according to
spectral coverage, and exactly reproducing the structure of the original
library by Pickles. Subdirectory dat_uvi  groups all spectra derived
from all ultraviolet, optical and near infrared sources, in the wavelength
range 1150-10620 Angstrom. This library has complete spectral coverage for
all components over this wavelength range, and is (in the original library)
referred to as UVILIB. Subdirectory dat_uvk groups all spectra that were
derived by combining the UVILIB spectra with additional infrared data to a
long wavelength limit of 25000 Angstrom. This is originally referred to as
UVKLIB. Within each subdirectory each spectrum is given in STSDAS table
format: the first column gives the wavelength for the given spectral range,
and the second column gives the flux. Fluxes are tabulated in units of
erg/s/cm^2/A and were calculated by normalizing the original fluxes in the
Pickles V band to a 0 magnitude in vegamag. In the vegamag system, Vega has
magnitude zero in all passbands.

For the UVILIB spectra, the names of the files are given as pickles_ttt.fits
where "pickles", for Pickles, is the library identifier and "ttt" is a number
ranging from 1 to 131. For the UVKLIB spectra, the names have the format
pickles_uk_ttt.fits, following the same nomenclature, and with the suffix
"uk" provided as to distinguish them from the shorter wavelength library.

The complete list of stars of different spectral type and luminosity class
together with the corresponding Pickles file is presented in Table 2.
The effective temperature information is extracted from Table 2 of Pickles
(1998). A "w" or an "r" preceding the spectral type indicates a
"weak" or "rich" metallicity in respect to solar. 

Table 2: Spectral type and Effective temperature corresponding to the Pickles
spectra in the library.

FILENAME      SPTYPE    EFF TEMP.
                         (K)
pickles_uk_1    O5V     39810.7
pickles_uk_2    O9V     35481.4
pickles_uk_3    B0V     28183.8
pickles_uk_4    B1V     22387.2
pickles_uk_5    B3V     19054.6
pickles_uk_6    B5-7V   14125.4
pickles_uk_7    B8V     11749.0
pickles_uk_9    A0V     9549.93
pickles_uk_10   A2V     8912.51
pickles_uk_11   A3V     8790.23
pickles_uk_12   A5V     8491.80
pickles_uk_14   F0V     7211.08
pickles_uk_15   F2V     6776.42
pickles_uk_16   F5V     6531.31
pickles_uk_20   F8V     6039.48
pickles_uk_23   G0V     5807.64
pickles_uk_26   G2V     5636.38
pickles_uk_27   G5V     5584.70
pickles_uk_30   G8V     5333.35
pickles_uk_31   K0V     5188.00
pickles_uk_33   K2V     4886.52
pickles_uk_36   K5V     4187.94
pickles_uk_37   K7V     3999.45
pickles_uk_38   M0V     3801.89
pickles_uk_40   M2V     3548.13
pickles_uk_43   M4V     3111.72
pickles_uk_44   M5V     2951.21
pickles_uk_46   B2IV    19952.6
pickles_uk_47   B6IV    12589.3
pickles_uk_48   A0IV    9727.47
pickles_uk_49   A4-7IV  7943.28
pickles_uk_50   F0-2IV  7030.72
pickles_uk_51   F5IV    6561.45
pickles_uk_52   F8IV    6151.77
pickles_uk_53   G0IV    5929.25
pickles_uk_54   G2IV    5688.53
pickles_uk_55   G5IV    5597.57
pickles_uk_56   G8IV    5308.84
pickles_uk_57   K0IV    5011.87
pickles_uk_58   K1IV    4786.30
pickles_uk_59   K3IV    4570.88
pickles_uk_60   O8III   31622.8
pickles_uk_61   B1-2III 19952.6
pickles_uk_63   B5III   14791.1
pickles_uk_64   B9III   11091.8
pickles_uk_65   A0III   9571.94
pickles_uk_67   A5III   8452.79
pickles_uk_69   F0III   7585.78
pickles_uk_71   F5III   6531.31
pickles_uk_72   G0III   5610.48
pickles_uk_73   G5III   5164.16
pickles_uk_76   G8III   5011.87
pickles_uk_78   K0III   4852.89
pickles_uk_87   K3III   4365.16
pickles_uk_93   K5III   4008.67
pickles_uk_95   M0III   3819.44
pickles_uk_100  M5III   3419.79
pickles_uk_105  M10III  2500.35
pickles_uk_106  B2II    15995.6
pickles_uk_107  B5II    12589.3
pickles_uk_108  F0II    7943.28
pickles_uk_109  F2II    7328.25
pickles_uk_110  G5II    5248.07
pickles_uk_111  K0-1II  5011.87
pickles_uk_112  K3-4II  4255.98
pickles_uk_113  M3II    3411.93
pickles_uk_114  B0I     26001.6
pickles_uk_117  B5I     13396.8
pickles_uk_118  B8I     11194.4
pickles_uk_119  A0I     9727.47
pickles_uk_121  F0I     7691.30
pickles_uk_122  F5I     6637.43
pickles_uk_123  F8I     6095.37
pickles_uk_124  G0I     5508.08
pickles_uk_126  G5I     5046.61
pickles_uk_127  G8I     4591.98
pickles_uk_128  K2I     4255.98
pickles_uk_130  K4I     3990.25
pickles_uk_131  M2I     3451.44

A similar list applies for the UKVKLIB library. For these spectra the names 
have the format "pickles_uk_ttt.fits". A reduced form of Table 2 can also 
be found in the library installed in CDBS and is named pickles.fits for the 
spectra in dat_uvi, and pickles_uk.fits for the spectra in dat_uvk directory.
A "w" or an "r" preceding the spectral type indicates a "weak" or "rich" 
metallicity in respect to solar. 


USE OF THE PICKLES STAR SPECTRA WITH SYNPHOT

Use of these spectra should be exactly similar to other libraries already
available in synphot. The desired spectrum is provided in input in any of
the synphot tasks as appropriate with no particular syntax. For examples on
how to use spectra from the synphot atlas library, please refer to the
Synphot Data User's Guide 
(http://www.stsci.edu/hst/HST_overview/documents/synphot/hst_synphot_cover.html).

APPENDIX

Below is an example of a standard header file for the spectrum
pickles_uk_51.fits. This spectrum corresponds to a star of spectral type
F5IV and covers a range in wavelength of 1150 to 25000 Angstrom
as can be assumed by the suffix "uk", which indicates a spectrum of the
UVKLIB library.

 1 SIMPLE   b T  Fits standard
 2 BITPIX   i 16  Bits per pixel
 3 NAXIS    i 0  Number of axes
 4 EXTEND   b T  File may contain extensions
 5 DATE     t '2007-01-11T21:02:21'  Date FITS file was generated
 6 IRAF-TLM t '16:02:37 (11/01/2007)'  Time of last modification
 7 COMMENT  t   FITS (Flexible Image Transport System) format is defined in 'Astronomy
 8 COMMENT  t   and Astrophysics', volume 376, page 359; bibcode: 2001A&A...376..359H
 9 ORIGIN   t 'STScI-STSDAS/TABLES'  Tables version 2002-02-22
10 FILENAME t 'pickles_uk_51.fits'  name of file
11 NEXTEND  i 1  number of extensions in file
12 COMMENT1 t spectral type: F5IV
13 COMMENT2 t metallicity: solar
14 COMMENT3 t original filename: ukf5iv.dat
15 HISTORY  t   File created by F.R.Boffi.
16 HISTORY  t   SEDs from Pickles UVKLIB Library (1998, PASP 110, 863).
17 HISTORY  t   Wavelength is in Angstrom.
18 HISTORY  t   Fluxes are tabulated in units of erg/s/cm2/A
19 HISTORY  t   and were calculated by normalizing the original fluxes
20 HISTORY  t   in the Pickles V band to a 0 magnitude in vegamag.
21 HISTORY  t   In the vegamag system, Vega has magnitude zero in all passbands.
22 HISTORY  t   Please refer to the SYNPHOT manual for further information.



