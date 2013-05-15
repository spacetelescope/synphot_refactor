"""Holds cases suggested by science oversight (Ralph Bohlin)."""

from pytools import testutil
import sys
import basecase

class S1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class S2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class S3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class S4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="crcalspec$g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

 
class stisS0(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g140l,fuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g230l,nuvmama,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g430l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g750l,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisS14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="stis,g230lb,ccd,s52x2"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class stisV1(basecase.countrateCase):
    def setUp(self):
        self.obsmode='stis,ccd'
        self.spectrum='rn(unit(1,flam),band(johnson,v),15.0,vegamag)'
        self.setglobal(__file__)
        self.runpy()


class acsS0(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS1(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS2(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f220w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS3(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS4(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS5(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f250w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS6(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS7(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS8(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS9(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS10(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS11(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS12(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS13(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS14(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS15(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS16(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS17(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS18(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS19(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS20(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS21(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS22(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS23(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f475w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS24(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS25(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS26(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS27(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS28(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS29(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS30(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS31(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS32(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f555w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS33(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS34(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS35(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS36(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS37(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS38(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f814w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS39(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS40(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS41(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f775w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS42(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS43(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS44(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS45(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS46(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS47(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f850lp"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS48(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS49(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS50(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f892n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS51(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS52(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS53(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS54(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS55(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS56(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f658n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS57(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS58(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS59(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS60(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS61(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS62(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS63(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS64(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS65(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f550m"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS66(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS67(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS68(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f435w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS69(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS70(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS71(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS72(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS73(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS74(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f344n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS75(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS76(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS77(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,hrc,f330w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS78(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS79(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS80(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f502n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS81(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS82(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS83(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f606w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS84(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS85(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS86(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f625w"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS87(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS88(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()
class acsS89(basecase.countrateCase):
    def setUp(self):
        self.obsmode="acs,wfc1,f660n"
        self.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        self.setglobal(__file__)
        self.runpy()

class e1(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el1215a.fits"
        self.setglobal(__file__)
        self.runpy()


class e2(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el1302a.fits"
        self.setglobal(__file__)
        self.runpy()

class e3(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el1356a.fits"
        self.setglobal(__file__)
        self.runpy()

class e4(basecase.countrateOverlapCase):
    def setUp(self):
        self.obsmode='stis,g140l,fuvmama,s52x2'
        self.spectrum="el2471a.fits"
        self.setglobal(__file__)
        self.runpy()


if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
