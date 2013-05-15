from pytools import testutil
import sys
import basecase


class E1photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E1flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E1fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E1vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E1abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E1stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E1obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E1counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E2photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E2flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E2fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E2vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E2abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E2stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E2obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E2counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E3photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E3flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E3fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E3vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E3abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E3stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E3obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E3counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E4photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E4flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E4fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E4vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E4abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E4stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E4obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E4counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E5photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E5flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E5fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E5vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E5abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E5stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E5obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E5counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E6photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E6flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E6fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E6vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E6abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E6stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E6obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E6counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E7photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E7flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E7fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E7vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E7abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E7stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E7obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E7counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E8photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E8flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E8fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E8vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E8abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E8stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E8obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E8counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E9photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E9flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E9fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E9vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E9abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E9stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E9obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E9counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E10photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E10flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E10fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E10vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E10abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E10stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E10obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E10counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E11photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E11flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E11fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E11vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E11abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E11stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E11obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E11counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E12photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E12flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E12fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E12vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E12abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E12stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E12obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E12counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E13photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E13flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E13fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E13vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E13abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E13stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E13obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E13counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E14photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E14flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E14fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E14vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E14abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E14stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E14obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E14counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E15photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E15flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E15fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E15vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E15abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E15stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E15obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E15counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E16photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E16flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E16fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E16vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E16abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E16stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E16obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E16counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E17photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E17flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E17fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E17vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E17abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E17stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E17obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E17counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E18photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E18flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E18fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E18vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E18abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E18stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E18obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E18counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E19photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E19flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E19fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E19vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E19abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E19stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E19obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E19counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E20photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E20flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E20fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E20vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E20abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E20stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E20obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E20counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E21photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E21flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E21fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E21vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E21abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E21stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E21obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E21counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E22photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E22flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E22fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E22vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E22abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E22stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E22obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E22counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E23photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E23flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E23fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E23vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E23abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E23stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E23obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E23counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E24photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E24flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E24fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E24vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E24abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E24stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E24obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E24counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E25photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E25flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E25fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E25vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E25abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E25stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E25obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E25counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E26photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E26flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E26fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E26vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E26abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E26stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E26obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E26counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E27photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E27flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E27fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E27vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E27abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E27stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E27obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E27counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E28photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E28flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E28fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E28vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E28abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E28stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E28obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E28counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E29photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E29flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E29fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E29vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E29abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E29stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E29obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E29counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E30photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E30flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E30fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E30vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E30abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E30stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E30obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E30counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E31photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E31flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E31fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E31vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E31abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E31stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E31obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E31counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E32photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E32flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E32fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E32vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E32abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E32stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E32obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E32counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E33photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E33flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E33fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E33vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E33abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E33stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E33obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E33counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E34photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E34flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E34fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E34vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E34abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E34stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E34obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E34counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E35photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E35flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E35fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E35vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E35abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E35stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E35obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E35counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E36photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E36flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E36fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E36vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E36abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E36stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E36obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E36counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E37photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E37flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E37fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E37vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E37abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E37stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E37obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E37counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E38photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E38flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E38fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E38vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E38abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E38stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E38obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E38counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E39photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E39flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E39fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E39vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E39abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E39stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E39obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E39counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E40photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E40flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E40fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E40vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E40abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E40stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E40obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E40counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E41photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E41flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E41fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E41vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E41abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E41stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E41obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E41counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E42photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E42flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E42fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E42vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E42abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E42stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E42obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E42counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E43photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E43flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E43fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E43vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E43abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E43stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E43obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E43counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E44photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E44flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E44fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E44vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E44abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E44stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E44obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E44counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E45photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E45flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E45fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E45vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E45abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E45stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E45obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E45counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E46photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E46flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E46fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E46vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E46abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E46stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E46obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E46counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E47photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E47flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E47fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E47vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E47abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E47stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E47obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E47counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E48photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E48flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E48fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E48vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E48abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E48stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E48obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E48counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E49photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E49flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E49fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E49vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E49abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E49stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E49obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E49counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E50photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E50flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E50fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E50vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E50abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E50stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E50obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E50counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E51photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E51flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E51fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E51vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E51abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E51stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E51obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E51counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E52photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E52flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E52fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E52vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E52abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E52stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E52obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E52counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E53photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E53flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E53fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E53vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E53abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E53stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E53obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E53counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E54photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E54flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E54fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E54vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E54abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E54stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E54obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E54counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E55photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E55flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E55fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E55vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E55abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E55stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E55obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E55counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E56photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E56flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E56fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E56vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E56abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E56stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E56obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E56counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E57photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E57flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E57fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E57vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E57abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E57stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E57obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E57counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E58photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E58flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E58fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E58vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E58abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E58stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E58obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E58counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E59photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E59flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E59fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E59vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E59abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E59stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E59obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E59counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E60photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E60flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E60fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E60vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E60abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E60stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E60obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E60counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E61photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E61flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E61fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E61vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E61abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E61stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E61obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E61counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E62photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E62flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E62fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E62vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E62abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E62stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E62obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E62counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E63photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E63flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E63fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E63vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E63abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E63stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E63obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E63counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E64photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E64flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E64fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E64vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E64abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E64stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E64obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E64counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E65photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E65flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E65fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E65vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E65abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E65stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E65obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E65counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E66photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E66flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E66fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E66vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E66abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E66stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E66obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E66counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E67photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E67flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E67fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E67vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E67abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E67stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E67obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E67counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E68photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E68flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E68fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E68vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E68abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E68stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E68obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E68counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E69photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E69flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E69fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E69vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E69abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E69stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E69obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E69counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E70photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E70flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E70fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E70vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E70abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E70stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E70obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E70counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E71photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E71flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E71fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E71vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E71abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E71stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E71obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E71counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E72photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E72flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E72fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E72vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E72abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E72stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E72obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E72counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E73photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E73flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E73fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E73vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E73abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E73stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E73obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E73counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E74photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E74flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E74fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E74vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E74abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E74stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E74obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E74counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E75photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E75flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E75fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E75vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E75abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E75stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E75obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E75counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E76photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E76flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E76fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E76vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E76abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E76stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E76obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E76counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E77photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E77flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E77fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E77vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E77abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E77stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E77obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E77counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E78photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E78flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E78fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E78vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E78abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E78stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E78obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E78counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E79photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E79flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E79fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E79vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E79abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E79stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E79obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E79counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E80photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E80flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E80fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E80vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E80abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E80stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E80obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E80counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E81photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E81flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E81fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E81vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E81abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E81stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E81obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E81counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E82photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E82flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E82fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E82vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E82abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E82stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E82obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E82counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E83photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E83flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E83fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E83vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E83abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E83stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E83obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E83counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E84photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E84flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E84fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E84vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E84abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E84stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E84obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E84counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E85photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E85flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E85fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E85vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E85abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E85stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E85obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E85counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E86photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E86flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E86fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E86vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E86abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E86stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E86obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E86counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E87photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E87flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E87fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E87vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E87abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E87stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E87obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E87counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E88photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E88flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E88fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E88vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E88abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E88stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E88obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E88counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E89photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E89flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E89fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E89vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E89abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E89stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E89obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E89counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E90photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E90flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E90fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E90vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E90abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E90stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E90obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E90counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E91photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E91flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E91fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E91vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E91abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E91stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E91obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E91counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E92photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E92flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E92fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E92vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E92abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E92stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E92obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E92counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E93photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E93flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E93fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E93vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E93abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E93stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E93obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E93counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E94photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E94flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E94fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E94vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E94abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E94stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E94obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E94counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E95photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E95flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E95fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E95vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E95abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E95stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E95obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E95counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E96photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E96flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E96fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E96vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E96abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E96stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E96obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E96counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E97photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E97flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E97fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E97vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E97abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E97stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E97obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E97counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E98photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E98flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E98fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E98vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E98abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E98stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E98obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E98counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E99photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E99flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E99fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E99vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E99abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E99stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E99obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E99counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E100photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E100flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E100fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E100vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E100abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E100stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E100obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E100counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E101photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E101flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E101fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E101vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E101abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E101stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E101obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E101counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E102photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E102flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E102fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E102vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E102abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E102stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E102obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E102counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E103photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E103flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E103fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E103vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E103abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E103stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E103obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E103counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E104photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E104flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E104fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E104vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E104abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E104stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E104obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E104counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E105photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E105flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E105fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E105vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E105abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E105stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E105obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E105counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E106photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E106flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E106fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E106vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E106abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E106stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E106obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E106counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E107photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E107flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E107fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E107vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E107abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E107stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E107obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E107counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E108photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E108flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E108fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E108vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E108abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E108stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E108obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E108counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E109photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E109flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E109fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E109vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E109abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E109stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E109obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E109counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E110photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E110flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E110fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E110vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E110abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E110stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E110obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E110counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E111photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E111flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E111fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E111vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E111abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E111stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E111obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E111counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E112photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E112flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E112fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E112vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E112abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E112stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E112obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E112counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E113photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E113flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E113fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E113vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E113abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E113stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E113obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E113counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E114photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E114flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E114fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E114vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E114abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E114stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E114obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E114counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E115photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E115flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E115fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E115vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E115abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E115stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E115obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E115counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E116photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E116flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E116fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E116vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E116abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E116stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E116obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E116counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E117photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E117flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E117fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E117vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E117abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E117stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E117obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E117counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E118photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E118flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E118fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E118vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E118abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E118stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E118obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E118counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E119photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E119flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E119fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E119vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E119abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E119stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E119obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E119counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E120photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E120flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E120fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E120vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E120abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E120stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E120obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E120counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E121photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E121flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E121fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E121vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E121abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E121stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E121obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E121counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E122photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E122flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E122fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E122vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E122abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E122stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E122obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E122counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E123photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E123flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E123fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E123vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E123abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E123stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E123obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E123counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E124photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E124flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E124fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E124vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E124abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E124stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E124obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E124counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E125photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E125flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E125fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E125vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E125abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E125stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E125obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E125counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E126photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E126flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E126fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E126vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E126abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E126stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E126obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E126counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E127photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E127flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E127fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E127vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E127abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E127stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E127obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E127counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E128photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E128flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E128fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E128vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E128abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E128stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E128obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E128counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E129photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E129flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E129fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E129vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E129abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E129stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E129obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E129counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E130photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E130flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E130fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E130vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E130abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E130stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E130obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E130counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E131photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E131flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E131fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E131vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E131abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E131stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E131obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E131counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E132photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E132flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E132fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E132vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E132abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E132stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E132obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E132counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E133photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E133flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E133fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E133vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E133abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E133stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E133obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E133counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E134photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E134flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E134fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E134vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E134abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E134stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E134obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E134counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E135photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E135flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E135fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E135vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E135abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E135stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E135obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E135counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E136photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E136flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E136fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E136vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E136abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E136stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E136obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E136counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E137photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E137flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E137fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E137vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E137abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E137stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E137obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E137counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E138photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E138flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E138fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E138vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E138abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E138stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E138obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E138counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E139photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E139flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E139fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E139vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E139abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E139stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E139obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E139counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E140photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E140flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E140fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E140vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E140abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E140stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E140obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E140counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E141photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E141flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E141fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E141vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E141abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E141stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E141obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E141counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E142photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E142flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E142fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E142vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E142abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E142stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E142obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E142counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E143photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E143flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E143fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E143vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E143abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E143stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E143obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E143counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E144photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E144flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E144fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E144vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E144abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E144stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E144obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E144counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E145photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E145flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E145fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E145vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E145abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E145stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E145obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E145counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E146photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E146flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E146fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E146vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E146abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E146stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E146obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E146counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E147photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E147flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E147fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E147vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E147abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E147stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E147obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E147counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E148photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E148flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E148fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E148vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E148abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E148stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E148obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E148counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E149photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E149flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E149fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E149vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E149abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E149stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E149obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E149counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E150photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E150flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E150fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E150vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E150abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E150stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E150obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E150counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E151photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E151flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E151fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E151vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E151abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E151stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E151obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E151counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E152photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E152flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E152fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E152vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E152abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E152stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E152obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E152counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E153photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E153flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E153fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E153vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E153abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E153stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E153obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E153counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E154photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E154flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E154fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E154vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E154abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E154stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E154obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E154counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E155photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E155flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E155fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E155vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E155abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E155stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E155obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E155counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E156photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E156flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E156fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E156vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E156abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E156stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E156obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E156counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E157photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E157flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E157fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E157vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E157abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E157stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E157obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E157counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E158photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E158flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E158fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E158vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E158abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E158stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E158obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E158counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E159photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E159flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E159fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E159vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E159abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E159stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E159obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E159counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E160photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E160flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E160fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E160vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E160abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E160stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E160obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E160counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E161photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E161flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E161fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E161vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E161abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E161stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E161obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E161counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E162photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E162flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E162fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E162vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E162abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E162stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E162obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E162counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E163photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E163flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E163fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E163vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E163abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E163stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E163obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E163counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E164photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E164flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E164fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E164vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E164abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E164stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E164obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E164counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E165photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E165flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E165fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E165vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E165abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E165stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E165obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E165counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E166photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E166flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E166fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E166vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E166abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E166stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E166obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E166counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E167photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E167flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E167fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E167vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E167abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E167stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E167obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E167counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E168photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E168flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E168fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E168vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E168abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E168stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E168obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E168counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E169photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E169flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E169fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E169vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E169abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E169stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E169obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E169counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E170photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E170flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E170fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E170vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E170abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E170stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E170obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E170counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E171photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E171flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E171fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E171vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E171abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E171stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E171obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E171counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E172photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E172flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E172fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E172vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E172abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E172stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E172obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E172counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E173photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E173flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E173fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E173vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E173abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E173stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E173obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E173counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E174photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E174flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E174fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E174vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E174abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E174stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E174obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E174counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E175photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E175flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E175fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E175vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E175abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E175stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E175obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E175counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E176photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E176flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E176fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E176vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E176abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E176stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E176obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E176counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E177photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E177flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E177fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E177vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E177abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E177stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E177obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E177counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E178photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E178flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E178fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E178vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E178abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E178stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E178obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E178counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E179photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E179flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E179fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E179vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E179abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E179stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E179obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E179counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E180photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E180flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E180fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E180vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E180abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E180stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E180obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E180counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E181photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E181flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E181fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E181vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E181abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E181stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E181obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E181counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E182photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E182flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E182fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E182vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E182abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E182stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E182obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E182counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E183photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E183flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E183fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E183vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E183abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E183stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E183obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E183counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E184photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E184flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E184fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E184vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E184abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E184stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E184obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E184counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E185photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E185flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E185fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E185vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E185abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E185stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E185obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E185counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E186photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E186flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E186fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E186vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E186abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E186stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E186obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E186counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E187photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E187flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E187fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E187vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E187abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E187stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E187obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E187counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E188photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E188flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E188fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E188vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E188abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E188stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E188obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E188counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E189photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E189flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E189fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E189vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E189abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E189stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E189obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E189counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E190photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E190flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E190fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E190vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E190abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E190stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E190obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E190counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E191photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E191flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E191fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E191vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E191abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E191stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E191obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E191counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E192photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E192flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E192fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E192vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E192abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E192stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E192obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E192counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E193photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E193flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E193fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E193vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E193abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E193stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E193obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E193counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E194photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E194flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E194fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E194vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E194abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E194stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E194obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E194counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E195photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E195flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E195fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E195vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E195abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E195stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E195obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E195counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E196photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E196flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E196fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E196vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E196abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E196stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E196obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E196counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E197photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E197flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E197fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E197vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E197abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E197stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E197obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E197counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E198photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E198flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E198fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E198vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E198abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E198stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E198obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E198counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E199photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E199flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E199fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E199vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E199abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E199stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E199obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E199counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E200photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E200flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E200fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E200vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E200abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E200stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E200obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E200counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E201photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E201flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E201fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E201vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E201abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E201stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E201obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E201counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E202photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E202flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E202fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E202vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E202abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E202stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E202obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E202counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E203photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E203flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E203fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E203vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E203abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E203stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E203obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E203counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E204photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E204flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E204fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E204vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E204abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E204stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E204obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E204counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E205photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E205flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E205fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E205vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E205abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E205stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E205obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E205counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E206photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E206flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E206fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E206vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E206abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E206stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E206obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E206counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E207photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E207flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E207fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E207vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E207abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E207stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E207obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E207counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E208photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E208flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E208fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E208vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E208abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E208stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E208obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E208counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E209photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E209flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E209fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E209vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E209abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E209stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E209obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E209counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E210photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E210flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E210fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E210vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E210abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E210stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E210obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E210counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E211photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E211flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E211fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E211vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E211abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E211stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E211obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E211counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E212photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E212flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E212fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E212vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E212abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E212stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E212obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E212counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E213photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E213flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E213fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E213vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E213abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E213stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E213obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E213counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E214photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E214flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E214fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E214vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E214abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E214stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E214obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E214counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E215photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E215flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E215fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E215vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E215abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E215stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E215obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E215counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E216photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E216flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E216fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E216vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E216abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E216stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E216obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E216counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E217photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E217flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E217fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E217vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E217abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E217stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E217obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E217counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E218photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E218flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E218fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E218vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E218abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E218stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E218obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E218counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E219photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E219flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E219fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E219vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E219abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E219stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E219obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E219counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E220photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E220flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E220fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E220vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E220abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E220stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E220obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E220counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E221photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E221flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E221fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E221vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E221abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E221stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E221obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E221counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E222photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E222flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E222fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E222vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E222abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E222stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E222obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E222counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E223photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E223flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E223fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E223vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E223abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E223stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E223obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E223counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E224photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E224flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E224fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E224vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E224abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E224stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E224obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E224counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E225photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E225flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E225fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E225vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E225abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E225stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E225obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E225counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E226photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E226flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E226fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E226vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E226abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E226stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E226obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E226counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E227photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E227flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E227fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E227vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E227abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E227stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E227obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E227counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E228photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E228flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E228fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E228vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E228abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E228stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E228obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E228counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E229photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E229flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E229fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E229vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E229abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E229stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E229obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E229counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E230photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E230flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E230fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E230vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E230abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E230stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E230obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E230counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E231photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E231flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E231fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E231vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E231abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E231stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E231obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E231counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E232photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E232flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E232fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E232vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E232abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E232stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E232obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E232counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E233photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E233flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E233fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E233vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E233abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E233stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E233obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E233counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E234photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E234flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E234fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E234vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E234abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E234stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E234obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E234counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E235photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E235flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E235fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E235vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E235abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E235stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E235obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E235counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E236photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E236flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E236fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E236vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E236abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E236stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E236obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E236counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E237photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E237flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E237fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E237vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E237abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E237stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E237obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E237counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E238photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E238flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E238fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E238vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E238abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E238stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E238obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E238counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E239photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E239flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E239fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E239vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E239abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E239stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E239obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E239counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E240photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E240flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E240fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E240vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E240abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E240stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E240obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E240counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E241photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E241flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E241fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E241vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E241abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E241stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E241obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E241counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E242photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E242flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E242fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E242vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E242abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E242stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E242obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E242counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E243photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E243flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E243fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E243vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E243abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E243stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E243obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E243counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E244photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E244flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E244fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E244vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E244abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E244stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E244obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E244counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E245photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E245flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E245fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E245vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E245abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E245stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E245obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E245counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E246photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E246flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E246fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E246vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E246abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E246stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E246obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E246counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E247photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E247flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E247fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E247vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E247abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E247stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E247obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E247counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E248photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E248flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E248fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E248vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E248abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E248stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E248obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E248counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E249photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E249flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E249fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E249vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E249abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E249stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E249obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E249counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E250photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E250flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E250fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E250vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E250abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E250stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E250obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E250counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E251photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E251flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E251fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E251vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E251abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E251stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E251obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E251counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E252photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E252flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E252fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E252vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E252abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E252stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E252obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E252counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E253photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E253flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E253fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E253vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E253abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E253stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E253obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E253counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E254photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E254flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E254fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E254vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E254abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E254stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E254obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E254counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E255photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E255flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E255fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E255vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E255abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E255stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E255obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E255counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E256photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E256flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E256fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E256vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E256abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E256stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E256obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E256counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E257photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E257flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E257fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E257vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E257abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E257stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E257obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E257counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E258photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E258flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E258fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E258vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E258abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E258stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E258obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E258counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E259photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E259flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E259fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E259vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E259abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E259stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E259obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E259counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E260photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E260flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E260fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E260vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E260abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E260stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E260obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E260counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E261photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E261flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E261fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E261vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E261abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E261stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E261obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E261counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E262photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E262flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E262fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E262vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E262abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E262stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E262obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E262counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E263photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E263flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E263fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E263vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E263abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E263stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E263obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E263counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E264photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E264flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E264fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E264vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E264abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E264stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E264obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E264counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E265photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E265flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E265fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E265vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E265abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E265stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E265obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E265counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E266photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E266flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E266fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E266vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E266abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E266stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E266obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E266counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E267photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E267flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E267fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E267vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E267abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E267stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E267obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E267counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,nuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E268photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E268flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E268fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E268vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E268abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E268stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E268obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E268counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E269photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E269flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E269fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E269vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E269abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E269stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E269obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E269counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E270photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E270flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E270fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E270vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E270abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E270stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E270obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E270counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E271photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E271flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E271fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E271vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E271abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E271stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E271obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E271counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E272photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E272flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E272fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E272vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E272abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E272stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E272obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E272counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E273photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E273flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E273fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E273vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E273abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E273stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E273obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E273counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E274photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E274flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E274fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E274vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E274abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E274stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E274obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E274counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="galex,fuv"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E275photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E275flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E275fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E275vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E275abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E275stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E275obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E275counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E276photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E276flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E276fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E276vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E276abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E276stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E276obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E276counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E277photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E277flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E277fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E277vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E277abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E277stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E277obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E277counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E278photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E278flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E278fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E278vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E278abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E278stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E278obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E278counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E279photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E279flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E279fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E279vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E279abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E279stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E279obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E279counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E280photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E280flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E280fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E280vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E280abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E280stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E280obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E280counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E281photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E281flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E281fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E281vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E281abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E281stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E281obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E281counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="stis,e140h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E282photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E282flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E282fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E282vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E282abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E282stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E282obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E282counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="stis,e140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E283photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E283flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E283fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E283vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E283abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E283stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E283obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E283counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="stis,e230h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E284photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E284flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E284fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E284vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E284abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E284stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E284obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E284counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="stis,e230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E285photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E285flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E285fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E285vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E285abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E285stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E285obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E285counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="stis,g140m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E286photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E286flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E286fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E286vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E286abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E286stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E286obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E286counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="stis,g230m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E287photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E287flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E287fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E287vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E287abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E287stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E287obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E287counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E288photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E288flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E288fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E288vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E288abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E288stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E288obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E288counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E289photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E289flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E289fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E289vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E289abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E289stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E289obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E289counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E290photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E290flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E290fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E290vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E290abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E290stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E290obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E290counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E291photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E291flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E291fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E291vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E291abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E291stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E291obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E291counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E292photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E292flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E292fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E292vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E292abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E292stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E292obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E292counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E293photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E293flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E293fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E293vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E293abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E293stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E293obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E293counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E294photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E294flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E294fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E294vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E294abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E294stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E294obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E294counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,37000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E295photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E295flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E295fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E295vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E295abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E295stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E295obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E295counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,35000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E296photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E296flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E296fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E296vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E296abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E296stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E296obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E296counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,30000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E297photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E297flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E297fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E297vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E297abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E297stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E297obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E297counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,25000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E298photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E298flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E298fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E298vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E298abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E298stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E298obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E298counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,20000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E299photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E299flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E299fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E299vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E299abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E299stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E299obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E299counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models,10000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E300photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E300flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E300fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E300vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E300abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E300stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E300obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E300counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="icat(k93models, 5000,0.0,4.0) "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E301photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E301flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E301fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E301vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E301abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E301stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E301obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E301counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E302photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E302flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E302fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E302vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E302abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E302stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E302obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E302counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E303photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E303flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E303fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E303vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E303abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E303stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E303obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E303counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E304photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E304flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E304fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E304vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E304abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E304stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E304obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E304counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E305photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E305flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E305fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E305vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E305abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E305stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E305obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E305counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E306photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E306flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E306fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E306vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E306abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E306stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E306obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E306counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,fuv,g130m,c1300"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E307photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E307flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E307fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E307vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E307abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E307stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E307obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E307counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb1_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E308photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E308flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E308fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E308vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E308abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E308stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E308obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E308counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb2_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E309photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E309flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E309fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E309vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E309abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E309stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E309obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E309counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb3_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E310photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E310flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E310fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E310vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E310abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E310stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E310obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E310counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb4_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E311photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E311flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E311fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E311vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E311abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E311stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E311obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E311counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb5_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E312photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E312flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E312fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E312vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E312abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E312stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E312obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E312counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$starb6_template.fits "
        self.obsmode="cos,nuv,g185m,c1835"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()

