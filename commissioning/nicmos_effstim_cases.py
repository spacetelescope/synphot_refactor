from pytools import testutil
import sys
import basecase


class E1photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E1flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E1fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E1vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E1abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E1stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E1obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E1counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E2photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E2flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E2fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E2vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E2abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E2stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E2obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E2counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E3photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E3flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E3fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E3vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E3abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E3stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E3obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E3counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E4photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E4flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E4fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E4vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E4abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E4stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E4obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E4counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,3,f110w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E5photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E5flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E5fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E5vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E5abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E5stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E5obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E5counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E6photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E6flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E6fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E6vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E6abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E6stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E6obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E6counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E7photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E7flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E7fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E7vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E7abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E7stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E7obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E7counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,k"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E8photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E8flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E8fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E8vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E8abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E8stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E8obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E8counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E9photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E9flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E9fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E9vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E9abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E9stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E9obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E9counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E10photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E10flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E10fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E10vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E10abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E10stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E10obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E10counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E11photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E11flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E11fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E11vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E11abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E11stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E11obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E11counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E12photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E12flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E12fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E12vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E12abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E12stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E12obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E12counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E13photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E13flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E13fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E13vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E13abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E13stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E13obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E13counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E14photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E14flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E14fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E14vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E14abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E14stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E14obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E14counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E15photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E15flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E15fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E15vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E15abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E15stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E15obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E15counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E16photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E16flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E16fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E16vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E16abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E16stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E16obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E16counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E17photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E17flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E17fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E17vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E17abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E17stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E17obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E17counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E18photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E18flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E18fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E18vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E18abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E18stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E18obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E18counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,2,f237m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E19photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E19flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E19fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E19vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E19abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E19stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E19obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E19counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E20photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E20flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E20fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E20vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E20abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E20stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E20obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E20counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.5) "
        self.obsmode="nicmos,2,f237m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E21photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E21flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E21fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E21vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E21abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E21stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E21obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E21counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E22photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E22flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E22fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E22vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E22abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E22stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E22obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E22counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="crgridkc96$sb_template.fits "
        self.obsmode="nicmos,1,f090m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E23photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E23flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E23fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E23vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E23abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E23stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E23obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E23counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.0) "
        self.obsmode="nicmos,2,f237m"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E24photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E24flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E24fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E24vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E24abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E24stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E24obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E24counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="bessell,h"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E25photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E25flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E25fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E25vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E25abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E25stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E25obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E25counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="bb(5000) "
        self.obsmode="nicmos,3,f108n"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E26photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E26flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E26fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E26vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E26abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E26stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E26obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E26counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,2.5) "
        self.obsmode="nicmos,3,f215n"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()


class E27photlam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="photlam"
        self.setglobal(__file__)
        self.runpy()


class E27flam(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="flam"
        self.setglobal(__file__)
        self.runpy()


class E27fnu(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="fnu"
        self.setglobal(__file__)
        self.runpy()


class E27vegamag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="vegamag"
        self.setglobal(__file__)
        self.runpy()


class E27abmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="abmag"
        self.setglobal(__file__)
        self.runpy()


class E27stmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="stmag"
        self.setglobal(__file__)
        self.runpy()


class E27obmag(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="obmag"
        self.setglobal(__file__)
        self.runpy()


class E27counts(basecase.effstimCase):
    def setUp(self):
        self.spectrum="z(crgridkc96$sb_template.fits,1.0) "
        self.obsmode="nicmos,2,f205w"
        self.form="counts"
        self.setglobal(__file__)
        self.runpy()

