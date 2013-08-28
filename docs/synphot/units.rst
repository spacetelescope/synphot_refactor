.. _synphot_units:

Photometry Units
================

These are the flux units used by ``synphot``:

    ===========================  ============================
    Flux representation          Unit
    ===========================  ============================
    ``synphot.units.PHOTLAM``    photon s^-1 cm^-2 A^-1
    ``synphot.units.PHOTNU``     photon s^-1 cm^-2 Hz^-1
    ``synphot.units.FLAM``       erg s^-1 cm^-2 A^-1
    ``synphot.units.FNU``        erg s^-1 cm^-2 Hz^-1
    ``synphot.units.STMAG``      -2.5 * log10(FLAM) - 21.10
    ``synphot.units.ABMAG``      -2.5 * log10(FNU)  - 48.60
    ``synphot.units.OBMAG``      -2.5 * log10(count)
    ``synphot.units.VEGAMAG``    -2.5 * log10(flux/flux_vega)
    ``astropy.units.count``      photon s^-1
    ``astropy.units.Jy``         10^-23 erg s^-1 cm^-2 Hz^-1
    ===========================  ============================

These are the magnitude zeropoints:

    ========================  =======  =========
    Zeropoint                 Used by  Value
    ========================  =======  =========
    ``synphot.units.STZERO``  STMAG    -21.1 mag
    ``synphot.units.ABZERO``  ABMAG    -48.6 mag
    ========================  =======  =========

These is a special dimensionless unit:

    * ``synphot.units.THROUGHPUT`` - Passband and extinction curve


.. _synphot-wave-conversion:

Wavelength Conversion
---------------------

``synphot.units.wave_conversion`` equivalencies are used for wavelength
conversion between length, wave number, and frequency, as shown in
examples below:

>>> Insert examples here


.. _synphot-flux-conversion:

Flux Conversion
---------------

Table below shows the supported flux conversions using equivalencies in
`synphot.units`. For simplicity, PHOTLAM is assigned the primary flux unit.

:func:`synphot.spectrum.convert_fluxes` can convert from one arbitrary flux unit
to another by first converting the input flux to PHOTLAM, and then to the
desired unit. The exception is conversion between two units with the same known
physical types (FNU and Jy), which is done directly via
:func:`astropy.units.core.Unit.to`. Different prefixes of Jy are also supported
by the function but not the equivalencies.

    +------------+------------------------------------------+
    | Input unit | Allowed output unit                      |
    +============+==========================================+
    | PHOTLAM    | PHOTNU, FLAM, FNU, STMAG, ABMAG, OBMAG,  |
    |            | VEGAMAG, count, Jy                       |
    +------------+------------------------------------------+
    | PHOTNU     | PHOTLAM                                  |
    +------------+------------------------------------------+
    | FLAM       | PHOTLAM                                  |
    +------------+------------------------------------------+
    | FNU        | PHOTLAM, Jy                              |
    +------------+------------------------------------------+
    | STMAG      | PHOTLAM                                  |
    +------------+------------------------------------------+
    | ABMAG      | PHOTLAM                                  |
    +------------+------------------------------------------+
    | OBMAG      | PHOTLAM                                  |
    +------------+------------------------------------------+
    | VEGAMAG    | PHOTLAM                                  |
    +------------+------------------------------------------+
    | Jy         | PHOTLAM, FNU                             |
    +------------+------------------------------------------+
    | count      | PHOTLAM                                  |
    +------------+------------------------------------------+

These are the constants used in some conversions:

    ====================  ==============================
    Constant              Descriptions
    ====================  ==============================
    ``synphot.units.H``   Planck's constant in CGS units
    ``synphot.units.C``   Speed of light in A/s
    ``synphot.units.HC``  H * C
    ====================  ==============================

Examples:

>>> Insert examples here
