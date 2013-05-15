from pytools import testutil
import sys
import basecase


class E1photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E1flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E1fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E1vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E1abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E1stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E1obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E1counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E2photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E2flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E2fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E2vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E2abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E2stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E2obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E2counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E3photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E3flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E3fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E3vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E3abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E3stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E3obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E3counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E4photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E4flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E4fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E4vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E4abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E4stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E4obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E4counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E5photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E5flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E5fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E5vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E5abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E5stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E5obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E5counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E6photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E6flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E6fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E6vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E6abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E6stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E6obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E6counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E7photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E7flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E7fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E7vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E7abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E7stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E7obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E7counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E8photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E8flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E8fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E8vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E8abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E8stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E8obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E8counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E9photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E9flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E9fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E9vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E9abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E9stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E9obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E9counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E10photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E10flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E10fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E10vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E10abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E10stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E10obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E10counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E11photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E11flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E11fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E11vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E11abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E11stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E11obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E11counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E12photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E12flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E12fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E12vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E12abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E12stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E12obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E12counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E13photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E13flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E13fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E13vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E13abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E13stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E13obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E13counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E14photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E14flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E14fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E14vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E14abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E14stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E14obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E14counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E15photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E15flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E15fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E15vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E15abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E15stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E15obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E15counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E16photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E16flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E16fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E16vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E16abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E16stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E16obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E16counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E17photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E17flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E17fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E17vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E17abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E17stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E17obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E17counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E18photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E18flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E18fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E18vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E18abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E18stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E18obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E18counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E19photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E19flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E19fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E19vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E19abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E19stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E19obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E19counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E20photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E20flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E20fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E20vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E20abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E20stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E20obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E20counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E21photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E21flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E21fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E21vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E21abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E21stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E21obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E21counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E22photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E22flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E22fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E22vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E22abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E22stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E22obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E22counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E23photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E23flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E23fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E23vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E23abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E23stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E23obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E23counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E24photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E24flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E24fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E24vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E24abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E24stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E24obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E24counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E25photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E25flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E25fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E25vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E25abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E25stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E25obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E25counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E26photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E26flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E26fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E26vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E26abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E26stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E26obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E26counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E27photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E27flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E27fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E27vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E27abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E27stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E27obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E27counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E28photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E28flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E28fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E28vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E28abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E28stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E28obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E28counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E29photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E29flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E29fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E29vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E29abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E29stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E29obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E29counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E30photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E30flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E30fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E30vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E30abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E30stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E30obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E30counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E31photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E31flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E31fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E31vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E31abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E31stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E31obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E31counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E32photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E32flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E32fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E32vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E32abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E32stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E32obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E32counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E33photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E33flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E33fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E33vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E33abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E33stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E33obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E33counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E34photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E34flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E34fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E34vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E34abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E34stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E34obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E34counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E35photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E35flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E35fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E35vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E35abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E35stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E35obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E35counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E36photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E36flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E36fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E36vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E36abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E36stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E36obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E36counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E37photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E37flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E37fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E37vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E37abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E37stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E37obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E37counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E38photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E38flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E38fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E38vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E38abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E38stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E38obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E38counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E39photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E39flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E39fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E39vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E39abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E39stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E39obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E39counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E40photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E40flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E40fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E40vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E40abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E40stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E40obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E40counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E41photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E41flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E41fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E41vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E41abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E41stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E41obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E41counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E42photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E42flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E42fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E42vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E42abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E42stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E42obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E42counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E43photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E43flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E43fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E43vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E43abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E43stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E43obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E43counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E44photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E44flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E44fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E44vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E44abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E44stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E44obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E44counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E45photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E45flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E45fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E45vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E45abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E45stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E45obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E45counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E46photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E46flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E46fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E46vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E46abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E46stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E46obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E46counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E47photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E47flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E47fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E47vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E47abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E47stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E47obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E47counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E48photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E48flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E48fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E48vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E48abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E48stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E48obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E48counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E49photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E49flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E49fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E49vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E49abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E49stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E49obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E49counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E50photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E50flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E50fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E50vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E50abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E50stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E50obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E50counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E51photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E51flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E51fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E51vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E51abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E51stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E51obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E51counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E52photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E52flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E52fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E52vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E52abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E52stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E52obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E52counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E53photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E53flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E53fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E53vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E53abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E53stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E53obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E53counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E54photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E54flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E54fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E54vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E54abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E54stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E54obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E54counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E55photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E55flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E55fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E55vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E55abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E55stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E55obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E55counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E56photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E56flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E56fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E56vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E56abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E56stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E56obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E56counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E57photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E57flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E57fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E57vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E57abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E57stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E57obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E57counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E58photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E58flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E58fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E58vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E58abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E58stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E58obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E58counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E59photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E59flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E59fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E59vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E59abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E59stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E59obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E59counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E60photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E60flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E60fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E60vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E60abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E60stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E60obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E60counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,wfc1,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E61photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E61flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E61fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E61vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E61abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E61stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E61obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E61counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E62photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E62flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E62fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E62vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E62abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E62stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E62obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E62counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E63photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E63flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E63fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E63vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E63abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E63stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E63obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E63counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E64photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E64flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E64fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E64vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E64abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E64stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E64obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E64counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E65photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E65flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E65fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E65vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E65abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E65stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E65obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E65counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E66photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E66flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E66fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E66vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E66abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E66stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E66obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E66counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E67photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E67flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E67fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E67vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E67abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E67stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E67obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E67counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E68photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E68flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E68fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E68vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E68abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E68stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E68obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E68counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E69photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E69flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E69fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E69vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E69abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E69stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E69obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E69counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E70photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E70flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E70fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E70vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E70abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E70stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E70obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E70counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E71photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E71flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E71fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E71vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E71abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E71stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E71obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E71counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E72photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E72flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E72fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E72vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E72abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E72stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E72obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E72counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E73photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E73flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E73fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E73vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E73abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E73stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E73obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E73counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E74photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E74flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E74fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E74vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E74abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E74stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E74obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E74counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E75photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E75flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E75fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E75vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E75abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E75stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E75obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E75counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E76photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E76flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E76fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E76vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E76abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E76stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E76obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E76counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E77photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E77flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E77fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E77vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E77abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E77stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E77obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E77counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E78photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E78flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E78fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E78vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E78abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E78stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E78obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E78counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E79photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E79flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E79fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E79vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E79abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E79stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E79obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E79counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E80photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E80flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E80fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E80vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E80abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E80stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E80obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E80counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E81photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E81flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E81fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E81vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E81abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E81stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E81obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E81counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E82photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E82flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E82fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E82vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E82abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E82stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E82obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E82counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E83photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E83flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E83fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E83vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E83abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E83stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E83obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E83counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E84photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E84flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E84fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E84vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E84abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E84stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E84obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E84counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E85photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E85flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E85fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E85vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E85abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E85stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E85obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E85counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E86photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E86flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E86fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E86vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E86abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E86stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E86obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E86counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E87photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E87flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E87fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E87vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E87abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E87stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E87obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E87counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E88photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E88flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E88fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E88vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E88abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E88stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E88obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E88counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E89photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E89flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E89fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E89vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E89abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E89stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E89obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E89counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E90photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E90flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E90fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E90vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E90abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E90stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E90obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E90counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E91photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E91flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E91fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E91vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E91abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E91stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E91obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E91counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E92photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E92flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E92fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E92vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E92abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E92stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E92obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E92counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E93photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E93flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E93fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E93vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E93abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E93stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E93obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E93counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E94photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E94flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E94fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E94vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E94abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E94stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E94obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E94counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E95photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E95flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E95fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E95vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E95abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E95stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E95obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E95counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E96photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E96flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E96fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E96vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E96abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E96stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E96obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E96counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E97photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E97flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E97fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E97vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E97abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E97stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E97obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E97counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E98photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E98flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E98fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E98vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E98abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E98stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E98obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E98counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E99photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E99flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E99fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E99vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E99abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E99stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E99obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E99counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E100photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E100flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E100fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E100vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E100abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E100stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E100obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E100counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E101photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E101flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E101fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E101vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E101abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E101stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E101obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E101counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E102photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E102flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E102fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E102vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E102abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E102stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E102obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E102counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E103photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E103flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E103fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E103vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E103abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E103stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E103obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E103counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E104photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E104flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E104fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E104vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E104abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E104stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E104obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E104counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E105photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E105flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E105fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E105vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E105abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E105stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E105obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E105counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E106photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E106flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E106fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E106vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E106abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E106stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E106obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E106counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E107photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E107flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E107fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E107vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E107abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E107stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E107obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E107counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E108photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E108flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E108fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E108vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E108abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E108stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E108obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E108counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E109photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E109flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E109fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E109vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E109abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E109stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E109obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E109counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(2000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E110photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E110flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E110fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E110vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E110abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E110stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E110obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E110counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E111photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E111flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E111fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E111vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E111abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E111stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E111obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E111counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E112photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E112flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E112fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E112vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E112abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E112stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E112obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E112counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E113photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E113flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E113fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E113vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E113abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E113stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E113obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E113counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(3000) "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E114photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E114flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E114fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E114vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E114abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E114stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E114obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E114counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f435w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E115photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E115flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E115fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E115vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E115abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E115stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E115obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E115counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f475w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E116photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E116flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E116fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E116vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E116abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E116stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E116obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E116counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f555w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E117photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E117flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E117fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E117vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E117abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E117stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E117obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E117counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f606w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E118photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E118flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E118fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E118vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E118abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E118stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E118obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E118counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f775w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E119photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E119flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E119fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E119vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E119abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E119stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E119obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E119counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f814w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E120photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E120flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E120fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E120vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E120abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E120stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E120obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E120counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crcalspec$alpha_lyr_stis_003.fits "
        self.obsmode="acs,hrc,f850lp"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()

