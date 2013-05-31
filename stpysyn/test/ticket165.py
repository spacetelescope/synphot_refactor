import pysynphot as S


def test_aper():
    olist=['wfc3,uvis1,f218w,aper#0.60',  # discovery case
           'wfc3,uvis1,f218w,aper#1.38',
           'wfc3,uvis1,f218w,aper#2.0',
           'wfc3,uvis2,f218w']  # should pass even before code is fixed

    for mode in olist:
        def makebp(mode):
            try:
                bp = S.ObsBandpass(mode)
            except KeyError,e:
                raise AssertionError(e.message)
        yield makebp, mode
