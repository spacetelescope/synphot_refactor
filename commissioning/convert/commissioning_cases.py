import sys
import conv_base

class TestComm1(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(10000)"
        cls.fname="C1_%s.fits"
        cls.setup2()

class TestComm2(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(5000)"
        cls.fname="C2_%s.fits"
        cls.setup2()

class TestComm3(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(5000.0)"
        cls.fname="C3_%s.fits"
        cls.setup2()

class TestComm4(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(50000)"
        cls.fname="C4_%s.fits"
        cls.setup2()

class TestComm5(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(5500)"
        cls.fname="C5_%s.fits"
        cls.setup2()

class TestComm6(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(6200)"
        cls.fname="C6_%s.fits"
        cls.setup2()

class TestComm7(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="bb(7700)"
        cls.fname="C7_%s.fits"
        cls.setup2()

class TestComm8(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(ck04models,15000,0.0,3.5)"
        cls.fname="C8_%s.fits"
        cls.setup2()

class TestComm9(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(ck04models,45000,0.0,4.5)"
        cls.fname="C9_%s.fits"
        cls.setup2()

class TestComm10(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(ck04models,4750,0.0,1.0)"
        cls.fname="C10_%s.fits"
        cls.setup2()

class TestComm11(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(ck04models,6250,0.0,4.5)"
        cls.fname="C11_%s.fits"
        cls.setup2()

class TestComm12(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(ck04models,7750,0.0,2.0)"
        cls.fname="C12_%s.fits"
        cls.setup2()

class TestComm13(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,11900,0.0,4.0)"
        cls.fname="C13_%s.fits"
        cls.setup2()

class TestComm14(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,15400,0.0,3.9)"
        cls.fname="C14_%s.fits"
        cls.setup2()

class TestComm15(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,18700,0.0,3.9)"
        cls.fname="C15_%s.fits"
        cls.setup2()

class TestComm16(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,25400,0.0,3.9)"
        cls.fname="C16_%s.fits"
        cls.setup2()

class TestComm17(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,30000,0.0,4.0)"
        cls.fname="C17_%s.fits"
        cls.setup2()

class TestComm18(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,33000.,0.0,4.0)"
        cls.fname="C18_%s.fits"
        cls.setup2()

class TestComm19(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,3500,0.0,4.6)"
        cls.fname="C19_%s.fits"
        cls.setup2()

class TestComm20(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,38000.,0.0,4.5)"
        cls.fname="C20_%s.fits"
        cls.setup2()

class TestComm21(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,4060,0.0,4.5)"
        cls.fname="C21_%s.fits"
        cls.setup2()

class TestComm22(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,44500,0.0,5.0)"
        cls.fname="C22_%s.fits"
        cls.setup2()

class TestComm23(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,4560,0.0,4.5)"
        cls.fname="C23_%s.fits"
        cls.setup2()

class TestComm24(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,4850,0.0,1.1)"
        cls.fname="C24_%s.fits"
        cls.setup2()

class TestComm25(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,5250,0.0,4.5)"
        cls.fname="C25_%s.fits"
        cls.setup2()

class TestComm26(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,5570,0.0,4.5)"
        cls.fname="C26_%s.fits"
        cls.setup2()

class TestComm27(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,5770,0.0,4.5)"
        cls.fname="C27_%s.fits"
        cls.setup2()

class TestComm28(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,5860,0.0,4.4)"
        cls.fname="C28_%s.fits"
        cls.setup2()

class TestComm29(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,6200,0.0,4.4)"
        cls.fname="C29_%s.fits"
        cls.setup2()

class TestComm30(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,6440,0.0,4.3)"
        cls.fname="C30_%s.fits"
        cls.setup2()

class TestComm31(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,6890,0.0,4.3)"
        cls.fname="C31_%s.fits"
        cls.setup2()

class TestComm32(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,7200,0.0,4.3)"
        cls.fname="C32_%s.fits"
        cls.setup2()

class TestComm33(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,7700,0.0,1.7)"
        cls.fname="C33_%s.fits"
        cls.setup2()

class TestComm34(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,8200,0.0,4.3)"
        cls.fname="C34_%s.fits"
        cls.setup2()

class TestComm35(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,8720,0.0,4.2)"
        cls.fname="C35_%s.fits"
        cls.setup2()

class TestComm36(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="icat(k93models,9230,0.0,4.1)"
        cls.fname="C36_%s.fits"
        cls.setup2()

class TestComm37(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="pl(4000.0,-0.5,flam)"
        cls.fname="C37_%s.fits"
        cls.setup2()

class TestComm38(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="pl(4000.0,-1.0,flam)"
        cls.fname="C38_%s.fits"
        cls.setup2()

class TestComm39(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="pl(4000.0,-1.5,flam)"
        cls.fname="C39_%s.fits"
        cls.setup2()

class TestComm40(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="pl(4000.0,-2.0,flam)"
        cls.fname="C40_%s.fits"
        cls.setup2()

class TestComm41(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="pl(4000.0,0.0,flam)"
        cls.fname="C41_%s.fits"
        cls.setup2()

class TestComm42(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, flam)"
        cls.fname="C42_%s.fits"
        cls.setup2()

class TestComm43(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, obmag)"
        cls.fname="C43_%s.fits"
        cls.setup2()

class TestComm44(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, photlam)"
        cls.fname="C44_%s.fits"
        cls.setup2()

class TestComm45(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F606W),29.0, vegamag)"
        cls.fname="C45_%s.fits"
        cls.setup2()

class TestComm46(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, flam)"
        cls.fname="C46_%s.fits"
        cls.setup2()

class TestComm47(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, obmag)"
        cls.fname="C47_%s.fits"
        cls.setup2()

class TestComm48(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, photlam)"
        cls.fname="C48_%s.fits"
        cls.setup2()

class TestComm49(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F775W),29.0, vegamag)"
        cls.fname="C49_%s.fits"
        cls.setup2()

class TestComm50(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, flam)"
        cls.fname="C50_%s.fits"
        cls.setup2()

class TestComm51(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, obmag)"
        cls.fname="C51_%s.fits"
        cls.setup2()

class TestComm52(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, photlam)"
        cls.fname="C52_%s.fits"
        cls.setup2()

class TestComm53(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F814W),29.0, vegamag)"
        cls.fname="C53_%s.fits"
        cls.setup2()

class TestComm54(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, flam)"
        cls.fname="C54_%s.fits"
        cls.setup2()

class TestComm55(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, obmag)"
        cls.fname="C55_%s.fits"
        cls.setup2()

class TestComm56(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, photlam)"
        cls.fname="C56_%s.fits"
        cls.setup2()

class TestComm57(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,HRC,F850LP),29.0, vegamag)"
        cls.fname="C57_%s.fits"
        cls.setup2()

class TestComm58(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, flam)"
        cls.fname="C58_%s.fits"
        cls.setup2()

class TestComm59(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, obmag)"
        cls.fname="C59_%s.fits"
        cls.setup2()

class TestComm60(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, photlam)"
        cls.fname="C60_%s.fits"
        cls.setup2()

class TestComm61(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F606W),29.0, vegamag)"
        cls.fname="C61_%s.fits"
        cls.setup2()

class TestComm62(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, flam)"
        cls.fname="C62_%s.fits"
        cls.setup2()

class TestComm63(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, obmag)"
        cls.fname="C63_%s.fits"
        cls.setup2()

class TestComm64(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, photlam)"
        cls.fname="C64_%s.fits"
        cls.setup2()

class TestComm65(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F775W),29.0, vegamag)"
        cls.fname="C65_%s.fits"
        cls.setup2()

class TestComm66(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, flam)"
        cls.fname="C66_%s.fits"
        cls.setup2()

class TestComm67(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, obmag)"
        cls.fname="C67_%s.fits"
        cls.setup2()

class TestComm68(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, photlam)"
        cls.fname="C68_%s.fits"
        cls.setup2()

class TestComm69(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F814W),29.0, vegamag)"
        cls.fname="C69_%s.fits"
        cls.setup2()

class TestComm70(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, flam)"
        cls.fname="C70_%s.fits"
        cls.setup2()

class TestComm71(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, obmag)"
        cls.fname="C71_%s.fits"
        cls.setup2()

class TestComm72(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, photlam)"
        cls.fname="C72_%s.fits"
        cls.setup2()

class TestComm73(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(2000),band(ACS,WFC1,F850LP),29.0, vegamag)"
        cls.fname="C73_%s.fits"
        cls.setup2()

class TestComm74(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, flam)"
        cls.fname="C74_%s.fits"
        cls.setup2()

class TestComm75(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, obmag)"
        cls.fname="C75_%s.fits"
        cls.setup2()

class TestComm76(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, photlam)"
        cls.fname="C76_%s.fits"
        cls.setup2()

class TestComm77(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F606W),29.0, vegamag)"
        cls.fname="C77_%s.fits"
        cls.setup2()

class TestComm78(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, flam)"
        cls.fname="C78_%s.fits"
        cls.setup2()

class TestComm79(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, obmag)"
        cls.fname="C79_%s.fits"
        cls.setup2()

class TestComm80(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, photlam)"
        cls.fname="C80_%s.fits"
        cls.setup2()

class TestComm81(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F775W),29.0, vegamag)"
        cls.fname="C81_%s.fits"
        cls.setup2()

class TestComm82(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, flam)"
        cls.fname="C82_%s.fits"
        cls.setup2()

class TestComm83(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, obmag)"
        cls.fname="C83_%s.fits"
        cls.setup2()

class TestComm84(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, photlam)"
        cls.fname="C84_%s.fits"
        cls.setup2()

class TestComm85(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F814W),29.0, vegamag)"
        cls.fname="C85_%s.fits"
        cls.setup2()

class TestComm86(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, flam)"
        cls.fname="C86_%s.fits"
        cls.setup2()

class TestComm87(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, obmag)"
        cls.fname="C87_%s.fits"
        cls.setup2()

class TestComm88(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, photlam)"
        cls.fname="C88_%s.fits"
        cls.setup2()

class TestComm89(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,HRC,F850LP),29.0, vegamag)"
        cls.fname="C89_%s.fits"
        cls.setup2()

class TestComm90(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, flam)"
        cls.fname="C90_%s.fits"
        cls.setup2()

class TestComm91(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, obmag)"
        cls.fname="C91_%s.fits"
        cls.setup2()

class TestComm92(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, photlam)"
        cls.fname="C92_%s.fits"
        cls.setup2()

class TestComm93(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F606W),29.0, vegamag)"
        cls.fname="C93_%s.fits"
        cls.setup2()

class TestComm94(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, flam)"
        cls.fname="C94_%s.fits"
        cls.setup2()

class TestComm95(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, obmag)"
        cls.fname="C95_%s.fits"
        cls.setup2()

class TestComm96(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, photlam)"
        cls.fname="C96_%s.fits"
        cls.setup2()

class TestComm97(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F775W),29.0, vegamag)"
        cls.fname="C97_%s.fits"
        cls.setup2()

class TestComm98(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, flam)"
        cls.fname="C98_%s.fits"
        cls.setup2()

class TestComm99(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, obmag)"
        cls.fname="C99_%s.fits"
        cls.setup2()

class TestComm100(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, photlam)"
        cls.fname="C100_%s.fits"
        cls.setup2()

class TestComm101(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F814W),29.0, vegamag)"
        cls.fname="C101_%s.fits"
        cls.setup2()

class TestComm102(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, flam)"
        cls.fname="C102_%s.fits"
        cls.setup2()

class TestComm103(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, obmag)"
        cls.fname="C103_%s.fits"
        cls.setup2()

class TestComm104(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, photlam)"
        cls.fname="C104_%s.fits"
        cls.setup2()

class TestComm105(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(3000),band(ACS,WFC1,F850LP),29.0, vegamag)"
        cls.fname="C105_%s.fits"
        cls.setup2()

class TestComm106(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),1.0e-14,photnu)"
        cls.fname="C106_%s.fits"
        cls.setup2()

class TestComm107(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),1.0e-27,fnu)"
        cls.fname="C107_%s.fits"
        cls.setup2()

class TestComm108(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),1.0e-4,photlam)"
        cls.fname="C108_%s.fits"
        cls.setup2()

class TestComm109(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),10,mjy)"
        cls.fname="C109_%s.fits"
        cls.setup2()

class TestComm110(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),18,stmag)"
        cls.fname="C110_%s.fits"
        cls.setup2()

class TestComm111(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),2.0e-7,jy)"
        cls.fname="C111_%s.fits"
        cls.setup2()

class TestComm112(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),23,abmag)"
        cls.fname="C112_%s.fits"
        cls.setup2()

class TestComm113(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),5,obmag)"
        cls.fname="C113_%s.fits"
        cls.setup2()

class TestComm114(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(bessell,h),5000,counts)"
        cls.fname="C114_%s.fits"
        cls.setup2()

class TestComm115(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(nicmos,2,f237m),25000,counts)"
        cls.fname="C115_%s.fits"
        cls.setup2()

class TestComm116(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(bb(5000),band(nicmos,3,f108n),30,mjy)"
        cls.fname="C116_%s.fits"
        cls.setup2()

class TestComm117(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, flam)"
        cls.fname="C117_%s.fits"
        cls.setup2()

class TestComm118(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, obmag)"
        cls.fname="C118_%s.fits"
        cls.setup2()

class TestComm119(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, photlam)"
        cls.fname="C119_%s.fits"
        cls.setup2()

class TestComm120(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F435W),29.0, vegamag)"
        cls.fname="C120_%s.fits"
        cls.setup2()

class TestComm121(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, flam)"
        cls.fname="C121_%s.fits"
        cls.setup2()

class TestComm122(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, obmag)"
        cls.fname="C122_%s.fits"
        cls.setup2()

class TestComm123(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, photlam)"
        cls.fname="C123_%s.fits"
        cls.setup2()

class TestComm124(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F475W),29.0, vegamag)"
        cls.fname="C124_%s.fits"
        cls.setup2()

class TestComm125(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, flam)"
        cls.fname="C125_%s.fits"
        cls.setup2()

class TestComm126(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, obmag)"
        cls.fname="C126_%s.fits"
        cls.setup2()

class TestComm127(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, photlam)"
        cls.fname="C127_%s.fits"
        cls.setup2()

class TestComm128(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F555W),29.0, vegamag)"
        cls.fname="C128_%s.fits"
        cls.setup2()

class TestComm129(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, flam)"
        cls.fname="C129_%s.fits"
        cls.setup2()

class TestComm130(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, obmag)"
        cls.fname="C130_%s.fits"
        cls.setup2()

class TestComm131(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, photlam)"
        cls.fname="C131_%s.fits"
        cls.setup2()

class TestComm132(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F606W),29.0, vegamag)"
        cls.fname="C132_%s.fits"
        cls.setup2()

class TestComm133(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, flam)"
        cls.fname="C133_%s.fits"
        cls.setup2()

class TestComm134(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, obmag)"
        cls.fname="C134_%s.fits"
        cls.setup2()

class TestComm135(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, photlam)"
        cls.fname="C135_%s.fits"
        cls.setup2()

class TestComm136(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F775W),29.0, vegamag)"
        cls.fname="C136_%s.fits"
        cls.setup2()

class TestComm137(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, flam)"
        cls.fname="C137_%s.fits"
        cls.setup2()

class TestComm138(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, obmag)"
        cls.fname="C138_%s.fits"
        cls.setup2()

class TestComm139(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, photlam)"
        cls.fname="C139_%s.fits"
        cls.setup2()

class TestComm140(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F814W),29.0, vegamag)"
        cls.fname="C140_%s.fits"
        cls.setup2()

class TestComm141(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, flam)"
        cls.fname="C141_%s.fits"
        cls.setup2()

class TestComm142(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, obmag)"
        cls.fname="C142_%s.fits"
        cls.setup2()

class TestComm143(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, photlam)"
        cls.fname="C143_%s.fits"
        cls.setup2()

class TestComm144(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,HRC,F850LP),29.0, vegamag)"
        cls.fname="C144_%s.fits"
        cls.setup2()

class TestComm145(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, flam)"
        cls.fname="C145_%s.fits"
        cls.setup2()

class TestComm146(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, obmag)"
        cls.fname="C146_%s.fits"
        cls.setup2()

class TestComm147(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, photlam)"
        cls.fname="C147_%s.fits"
        cls.setup2()

class TestComm148(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F435W),29.0, vegamag)"
        cls.fname="C148_%s.fits"
        cls.setup2()

class TestComm149(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, flam)"
        cls.fname="C149_%s.fits"
        cls.setup2()

class TestComm150(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, obmag)"
        cls.fname="C150_%s.fits"
        cls.setup2()

class TestComm151(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, photlam)"
        cls.fname="C151_%s.fits"
        cls.setup2()

class TestComm152(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F475W),29.0, vegamag)"
        cls.fname="C152_%s.fits"
        cls.setup2()

class TestComm153(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, flam)"
        cls.fname="C153_%s.fits"
        cls.setup2()

class TestComm154(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, obmag)"
        cls.fname="C154_%s.fits"
        cls.setup2()

class TestComm155(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, photlam)"
        cls.fname="C155_%s.fits"
        cls.setup2()

class TestComm156(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F555W),29.0, vegamag)"
        cls.fname="C156_%s.fits"
        cls.setup2()

class TestComm157(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, flam)"
        cls.fname="C157_%s.fits"
        cls.setup2()

class TestComm158(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, obmag)"
        cls.fname="C158_%s.fits"
        cls.setup2()

class TestComm159(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, photlam)"
        cls.fname="C159_%s.fits"
        cls.setup2()

class TestComm160(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F606W),29.0, vegamag)"
        cls.fname="C160_%s.fits"
        cls.setup2()

class TestComm161(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, flam)"
        cls.fname="C161_%s.fits"
        cls.setup2()

class TestComm162(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, obmag)"
        cls.fname="C162_%s.fits"
        cls.setup2()

class TestComm163(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, photlam)"
        cls.fname="C163_%s.fits"
        cls.setup2()

class TestComm164(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F775W),29.0, vegamag)"
        cls.fname="C164_%s.fits"
        cls.setup2()

class TestComm165(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, flam)"
        cls.fname="C165_%s.fits"
        cls.setup2()

class TestComm166(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, obmag)"
        cls.fname="C166_%s.fits"
        cls.setup2()

class TestComm167(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, photlam)"
        cls.fname="C167_%s.fits"
        cls.setup2()

class TestComm168(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F814W),29.0, vegamag)"
        cls.fname="C168_%s.fits"
        cls.setup2()

class TestComm169(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, flam)"
        cls.fname="C169_%s.fits"
        cls.setup2()

class TestComm170(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, obmag)"
        cls.fname="C170_%s.fits"
        cls.setup2()

class TestComm171(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, photlam)"
        cls.fname="C171_%s.fits"
        cls.setup2()

class TestComm172(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crcalspec$alpha_lyr_stis_003.fits,band(ACS,WFC1,F850LP),29.0, vegamag)"
        cls.fname="C172_%s.fits"
        cls.setup2()

class TestComm173(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),0.5,jy)"
        cls.fname="C173_%s.fits"
        cls.setup2()

class TestComm174(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.0e-14,photnu)"
        cls.fname="C174_%s.fits"
        cls.setup2()

class TestComm175(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.0e-4,photlam)"
        cls.fname="C175_%s.fits"
        cls.setup2()

class TestComm176(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),1.e-27,fnu)"
        cls.fname="C176_%s.fits"
        cls.setup2()

class TestComm177(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),10000,counts)"
        cls.fname="C177_%s.fits"
        cls.setup2()

class TestComm178(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,1,f090m),5,obmag)"
        cls.fname="C178_%s.fits"
        cls.setup2()

class TestComm179(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,3,f110w),18,stmag)"
        cls.fname="C179_%s.fits"
        cls.setup2()

class TestComm180(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$sb_template.fits,band(nicmos,3,f110w),23,abmag)"
        cls.fname="C180_%s.fits"
        cls.setup2()

class TestComm181(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C181_%s.fits"
        cls.setup2()

class TestComm182(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C182_%s.fits"
        cls.setup2()

class TestComm183(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C183_%s.fits"
        cls.setup2()

class TestComm184(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C184_%s.fits"
        cls.setup2()

class TestComm185(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C185_%s.fits"
        cls.setup2()

class TestComm186(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C186_%s.fits"
        cls.setup2()

class TestComm187(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C187_%s.fits"
        cls.setup2()

class TestComm188(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C188_%s.fits"
        cls.setup2()

class TestComm189(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C189_%s.fits"
        cls.setup2()

class TestComm190(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C190_%s.fits"
        cls.setup2()

class TestComm191(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C191_%s.fits"
        cls.setup2()

class TestComm192(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C192_%s.fits"
        cls.setup2()

class TestComm193(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.,mjy)"
        cls.fname="C193_%s.fits"
        cls.setup2()

class TestComm194(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.e-15,photnu)"
        cls.fname="C194_%s.fits"
        cls.setup2()

class TestComm195(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.e-26,fnu)"
        cls.fname="C195_%s.fits"
        cls.setup2()

class TestComm196(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),1.e-3,jy)"
        cls.fname="C196_%s.fits"
        cls.setup2()

class TestComm197(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),16.0,abmag)"
        cls.fname="C197_%s.fits"
        cls.setup2()

class TestComm198(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb1_template.fits,band(stis,e140h),16.0,stmag)"
        cls.fname="C198_%s.fits"
        cls.setup2()

class TestComm199(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C199_%s.fits"
        cls.setup2()

class TestComm200(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C200_%s.fits"
        cls.setup2()

class TestComm201(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C201_%s.fits"
        cls.setup2()

class TestComm202(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C202_%s.fits"
        cls.setup2()

class TestComm203(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C203_%s.fits"
        cls.setup2()

class TestComm204(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C204_%s.fits"
        cls.setup2()

class TestComm205(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C205_%s.fits"
        cls.setup2()

class TestComm206(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C206_%s.fits"
        cls.setup2()

class TestComm207(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C207_%s.fits"
        cls.setup2()

class TestComm208(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C208_%s.fits"
        cls.setup2()

class TestComm209(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C209_%s.fits"
        cls.setup2()

class TestComm210(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C210_%s.fits"
        cls.setup2()

class TestComm211(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.,mjy)"
        cls.fname="C211_%s.fits"
        cls.setup2()

class TestComm212(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.e-15,photnu)"
        cls.fname="C212_%s.fits"
        cls.setup2()

class TestComm213(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.e-26,fnu)"
        cls.fname="C213_%s.fits"
        cls.setup2()

class TestComm214(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),1.e-3,jy)"
        cls.fname="C214_%s.fits"
        cls.setup2()

class TestComm215(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),16.0,abmag)"
        cls.fname="C215_%s.fits"
        cls.setup2()

class TestComm216(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb2_template.fits,band(stis,e140m),16.0,stmag)"
        cls.fname="C216_%s.fits"
        cls.setup2()

class TestComm217(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C217_%s.fits"
        cls.setup2()

class TestComm218(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C218_%s.fits"
        cls.setup2()

class TestComm219(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C219_%s.fits"
        cls.setup2()

class TestComm220(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C220_%s.fits"
        cls.setup2()

class TestComm221(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C221_%s.fits"
        cls.setup2()

class TestComm222(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C222_%s.fits"
        cls.setup2()

class TestComm223(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C223_%s.fits"
        cls.setup2()

class TestComm224(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C224_%s.fits"
        cls.setup2()

class TestComm225(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C225_%s.fits"
        cls.setup2()

class TestComm226(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C226_%s.fits"
        cls.setup2()

class TestComm227(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C227_%s.fits"
        cls.setup2()

class TestComm228(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C228_%s.fits"
        cls.setup2()

class TestComm229(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.,mjy)"
        cls.fname="C229_%s.fits"
        cls.setup2()

class TestComm230(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.e-15,photnu)"
        cls.fname="C230_%s.fits"
        cls.setup2()

class TestComm231(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.e-26,fnu)"
        cls.fname="C231_%s.fits"
        cls.setup2()

class TestComm232(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),1.e-3,jy)"
        cls.fname="C232_%s.fits"
        cls.setup2()

class TestComm233(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),16.0,abmag)"
        cls.fname="C233_%s.fits"
        cls.setup2()

class TestComm234(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb3_template.fits,band(stis,e230h),16.0,stmag)"
        cls.fname="C234_%s.fits"
        cls.setup2()

class TestComm235(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C235_%s.fits"
        cls.setup2()

class TestComm236(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C236_%s.fits"
        cls.setup2()

class TestComm237(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C237_%s.fits"
        cls.setup2()

class TestComm238(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C238_%s.fits"
        cls.setup2()

class TestComm239(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C239_%s.fits"
        cls.setup2()

class TestComm240(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C240_%s.fits"
        cls.setup2()

class TestComm241(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C241_%s.fits"
        cls.setup2()

class TestComm242(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C242_%s.fits"
        cls.setup2()

class TestComm243(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C243_%s.fits"
        cls.setup2()

class TestComm244(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C244_%s.fits"
        cls.setup2()

class TestComm245(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C245_%s.fits"
        cls.setup2()

class TestComm246(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C246_%s.fits"
        cls.setup2()

class TestComm247(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.,mjy)"
        cls.fname="C247_%s.fits"
        cls.setup2()

class TestComm248(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.e-15,photnu)"
        cls.fname="C248_%s.fits"
        cls.setup2()

class TestComm249(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.e-26,fnu)"
        cls.fname="C249_%s.fits"
        cls.setup2()

class TestComm250(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),1.e-3,jy)"
        cls.fname="C250_%s.fits"
        cls.setup2()

class TestComm251(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),16.0,abmag)"
        cls.fname="C251_%s.fits"
        cls.setup2()

class TestComm252(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb4_template.fits,band(stis,e230m),16.0,stmag)"
        cls.fname="C252_%s.fits"
        cls.setup2()

class TestComm253(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C253_%s.fits"
        cls.setup2()

class TestComm254(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C254_%s.fits"
        cls.setup2()

class TestComm255(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C255_%s.fits"
        cls.setup2()

class TestComm256(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C256_%s.fits"
        cls.setup2()

class TestComm257(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C257_%s.fits"
        cls.setup2()

class TestComm258(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C258_%s.fits"
        cls.setup2()

class TestComm259(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C259_%s.fits"
        cls.setup2()

class TestComm260(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C260_%s.fits"
        cls.setup2()

class TestComm261(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C261_%s.fits"
        cls.setup2()

class TestComm262(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C262_%s.fits"
        cls.setup2()

class TestComm263(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C263_%s.fits"
        cls.setup2()

class TestComm264(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C264_%s.fits"
        cls.setup2()

class TestComm265(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.,mjy)"
        cls.fname="C265_%s.fits"
        cls.setup2()

class TestComm266(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.e-15,photnu)"
        cls.fname="C266_%s.fits"
        cls.setup2()

class TestComm267(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.e-26,fnu)"
        cls.fname="C267_%s.fits"
        cls.setup2()

class TestComm268(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),1.e-3,jy)"
        cls.fname="C268_%s.fits"
        cls.setup2()

class TestComm269(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),16.0,abmag)"
        cls.fname="C269_%s.fits"
        cls.setup2()

class TestComm270(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb5_template.fits,band(stis,g140m),16.0,stmag)"
        cls.fname="C270_%s.fits"
        cls.setup2()

class TestComm271(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C271_%s.fits"
        cls.setup2()

class TestComm272(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C272_%s.fits"
        cls.setup2()

class TestComm273(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C273_%s.fits"
        cls.setup2()

class TestComm274(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C274_%s.fits"
        cls.setup2()

class TestComm275(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C275_%s.fits"
        cls.setup2()

class TestComm276(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C276_%s.fits"
        cls.setup2()

class TestComm277(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C277_%s.fits"
        cls.setup2()

class TestComm278(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C278_%s.fits"
        cls.setup2()

class TestComm279(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C279_%s.fits"
        cls.setup2()

class TestComm280(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C280_%s.fits"
        cls.setup2()

class TestComm281(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C281_%s.fits"
        cls.setup2()

class TestComm282(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C282_%s.fits"
        cls.setup2()

class TestComm283(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.,mjy)"
        cls.fname="C283_%s.fits"
        cls.setup2()

class TestComm284(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.e-15,photnu)"
        cls.fname="C284_%s.fits"
        cls.setup2()

class TestComm285(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.e-26,fnu)"
        cls.fname="C285_%s.fits"
        cls.setup2()

class TestComm286(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),1.e-3,jy)"
        cls.fname="C286_%s.fits"
        cls.setup2()

class TestComm287(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),16.0,abmag)"
        cls.fname="C287_%s.fits"
        cls.setup2()

class TestComm288(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(crgridkc96$starb6_template.fits,band(stis,g230m),16.0,stmag)"
        cls.fname="C288_%s.fits"
        cls.setup2()

class TestComm289(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C289_%s.fits"
        cls.setup2()

class TestComm290(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C290_%s.fits"
        cls.setup2()

class TestComm291(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C291_%s.fits"
        cls.setup2()

class TestComm292(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C292_%s.fits"
        cls.setup2()

class TestComm293(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C293_%s.fits"
        cls.setup2()

class TestComm294(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C294_%s.fits"
        cls.setup2()

class TestComm295(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C295_%s.fits"
        cls.setup2()

class TestComm296(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C296_%s.fits"
        cls.setup2()

class TestComm297(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C297_%s.fits"
        cls.setup2()

class TestComm298(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C298_%s.fits"
        cls.setup2()

class TestComm299(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C299_%s.fits"
        cls.setup2()

class TestComm300(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C300_%s.fits"
        cls.setup2()

class TestComm301(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C301_%s.fits"
        cls.setup2()

class TestComm302(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C302_%s.fits"
        cls.setup2()

class TestComm303(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C303_%s.fits"
        cls.setup2()

class TestComm304(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C304_%s.fits"
        cls.setup2()

class TestComm305(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C305_%s.fits"
        cls.setup2()

class TestComm306(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C306_%s.fits"
        cls.setup2()

class TestComm307(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C307_%s.fits"
        cls.setup2()

class TestComm308(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C308_%s.fits"
        cls.setup2()

class TestComm309(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C309_%s.fits"
        cls.setup2()

class TestComm310(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C310_%s.fits"
        cls.setup2()

class TestComm311(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C311_%s.fits"
        cls.setup2()

class TestComm312(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models, 5000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C312_%s.fits"
        cls.setup2()

class TestComm313(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C313_%s.fits"
        cls.setup2()

class TestComm314(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C314_%s.fits"
        cls.setup2()

class TestComm315(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C315_%s.fits"
        cls.setup2()

class TestComm316(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C316_%s.fits"
        cls.setup2()

class TestComm317(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C317_%s.fits"
        cls.setup2()

class TestComm318(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C318_%s.fits"
        cls.setup2()

class TestComm319(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C319_%s.fits"
        cls.setup2()

class TestComm320(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C320_%s.fits"
        cls.setup2()

class TestComm321(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C321_%s.fits"
        cls.setup2()

class TestComm322(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C322_%s.fits"
        cls.setup2()

class TestComm323(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C323_%s.fits"
        cls.setup2()

class TestComm324(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C324_%s.fits"
        cls.setup2()

class TestComm325(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C325_%s.fits"
        cls.setup2()

class TestComm326(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C326_%s.fits"
        cls.setup2()

class TestComm327(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C327_%s.fits"
        cls.setup2()

class TestComm328(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C328_%s.fits"
        cls.setup2()

class TestComm329(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C329_%s.fits"
        cls.setup2()

class TestComm330(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C330_%s.fits"
        cls.setup2()

class TestComm331(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C331_%s.fits"
        cls.setup2()

class TestComm332(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C332_%s.fits"
        cls.setup2()

class TestComm333(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C333_%s.fits"
        cls.setup2()

class TestComm334(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C334_%s.fits"
        cls.setup2()

class TestComm335(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C335_%s.fits"
        cls.setup2()

class TestComm336(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,10000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C336_%s.fits"
        cls.setup2()

class TestComm337(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C337_%s.fits"
        cls.setup2()

class TestComm338(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C338_%s.fits"
        cls.setup2()

class TestComm339(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C339_%s.fits"
        cls.setup2()

class TestComm340(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C340_%s.fits"
        cls.setup2()

class TestComm341(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C341_%s.fits"
        cls.setup2()

class TestComm342(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C342_%s.fits"
        cls.setup2()

class TestComm343(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C343_%s.fits"
        cls.setup2()

class TestComm344(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C344_%s.fits"
        cls.setup2()

class TestComm345(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C345_%s.fits"
        cls.setup2()

class TestComm346(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C346_%s.fits"
        cls.setup2()

class TestComm347(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C347_%s.fits"
        cls.setup2()

class TestComm348(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C348_%s.fits"
        cls.setup2()

class TestComm349(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C349_%s.fits"
        cls.setup2()

class TestComm350(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C350_%s.fits"
        cls.setup2()

class TestComm351(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C351_%s.fits"
        cls.setup2()

class TestComm352(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C352_%s.fits"
        cls.setup2()

class TestComm353(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C353_%s.fits"
        cls.setup2()

class TestComm354(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C354_%s.fits"
        cls.setup2()

class TestComm355(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C355_%s.fits"
        cls.setup2()

class TestComm356(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C356_%s.fits"
        cls.setup2()

class TestComm357(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C357_%s.fits"
        cls.setup2()

class TestComm358(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C358_%s.fits"
        cls.setup2()

class TestComm359(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C359_%s.fits"
        cls.setup2()

class TestComm360(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,20000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C360_%s.fits"
        cls.setup2()

class TestComm361(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C361_%s.fits"
        cls.setup2()

class TestComm362(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C362_%s.fits"
        cls.setup2()

class TestComm363(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C363_%s.fits"
        cls.setup2()

class TestComm364(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C364_%s.fits"
        cls.setup2()

class TestComm365(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C365_%s.fits"
        cls.setup2()

class TestComm366(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C366_%s.fits"
        cls.setup2()

class TestComm367(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C367_%s.fits"
        cls.setup2()

class TestComm368(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C368_%s.fits"
        cls.setup2()

class TestComm369(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C369_%s.fits"
        cls.setup2()

class TestComm370(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C370_%s.fits"
        cls.setup2()

class TestComm371(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C371_%s.fits"
        cls.setup2()

class TestComm372(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C372_%s.fits"
        cls.setup2()

class TestComm373(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C373_%s.fits"
        cls.setup2()

class TestComm374(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C374_%s.fits"
        cls.setup2()

class TestComm375(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C375_%s.fits"
        cls.setup2()

class TestComm376(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C376_%s.fits"
        cls.setup2()

class TestComm377(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C377_%s.fits"
        cls.setup2()

class TestComm378(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C378_%s.fits"
        cls.setup2()

class TestComm379(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C379_%s.fits"
        cls.setup2()

class TestComm380(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C380_%s.fits"
        cls.setup2()

class TestComm381(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C381_%s.fits"
        cls.setup2()

class TestComm382(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C382_%s.fits"
        cls.setup2()

class TestComm383(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C383_%s.fits"
        cls.setup2()

class TestComm384(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,25000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C384_%s.fits"
        cls.setup2()

class TestComm385(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C385_%s.fits"
        cls.setup2()

class TestComm386(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C386_%s.fits"
        cls.setup2()

class TestComm387(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C387_%s.fits"
        cls.setup2()

class TestComm388(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C388_%s.fits"
        cls.setup2()

class TestComm389(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C389_%s.fits"
        cls.setup2()

class TestComm390(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C390_%s.fits"
        cls.setup2()

class TestComm391(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C391_%s.fits"
        cls.setup2()

class TestComm392(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C392_%s.fits"
        cls.setup2()

class TestComm393(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C393_%s.fits"
        cls.setup2()

class TestComm394(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C394_%s.fits"
        cls.setup2()

class TestComm395(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C395_%s.fits"
        cls.setup2()

class TestComm396(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C396_%s.fits"
        cls.setup2()

class TestComm397(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C397_%s.fits"
        cls.setup2()

class TestComm398(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C398_%s.fits"
        cls.setup2()

class TestComm399(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C399_%s.fits"
        cls.setup2()

class TestComm400(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C400_%s.fits"
        cls.setup2()

class TestComm401(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C401_%s.fits"
        cls.setup2()

class TestComm402(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C402_%s.fits"
        cls.setup2()

class TestComm403(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C403_%s.fits"
        cls.setup2()

class TestComm404(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C404_%s.fits"
        cls.setup2()

class TestComm405(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C405_%s.fits"
        cls.setup2()

class TestComm406(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C406_%s.fits"
        cls.setup2()

class TestComm407(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C407_%s.fits"
        cls.setup2()

class TestComm408(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C408_%s.fits"
        cls.setup2()

class TestComm409(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C409_%s.fits"
        cls.setup2()

class TestComm410(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C410_%s.fits"
        cls.setup2()

class TestComm411(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C411_%s.fits"
        cls.setup2()

class TestComm412(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C412_%s.fits"
        cls.setup2()

class TestComm413(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C413_%s.fits"
        cls.setup2()

class TestComm414(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C414_%s.fits"
        cls.setup2()

class TestComm415(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C415_%s.fits"
        cls.setup2()

class TestComm416(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C416_%s.fits"
        cls.setup2()

class TestComm417(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C417_%s.fits"
        cls.setup2()

class TestComm418(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C418_%s.fits"
        cls.setup2()

class TestComm419(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C419_%s.fits"
        cls.setup2()

class TestComm420(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C420_%s.fits"
        cls.setup2()

class TestComm421(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C421_%s.fits"
        cls.setup2()

class TestComm422(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C422_%s.fits"
        cls.setup2()

class TestComm423(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C423_%s.fits"
        cls.setup2()

class TestComm424(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C424_%s.fits"
        cls.setup2()

class TestComm425(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C425_%s.fits"
        cls.setup2()

class TestComm426(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C426_%s.fits"
        cls.setup2()

class TestComm427(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C427_%s.fits"
        cls.setup2()

class TestComm428(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C428_%s.fits"
        cls.setup2()

class TestComm429(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C429_%s.fits"
        cls.setup2()

class TestComm430(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C430_%s.fits"
        cls.setup2()

class TestComm431(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C431_%s.fits"
        cls.setup2()

class TestComm432(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,35000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C432_%s.fits"
        cls.setup2()

class TestComm433(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.,mjy)"
        cls.fname="C433_%s.fits"
        cls.setup2()

class TestComm434(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-15,photnu)"
        cls.fname="C434_%s.fits"
        cls.setup2()

class TestComm435(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-26,fnu)"
        cls.fname="C435_%s.fits"
        cls.setup2()

class TestComm436(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),1.e-3,jy)"
        cls.fname="C436_%s.fits"
        cls.setup2()

class TestComm437(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,abmag)"
        cls.fname="C437_%s.fits"
        cls.setup2()

class TestComm438(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,fuv,g130m,c1300),16.0,stmag)"
        cls.fname="C438_%s.fits"
        cls.setup2()

class TestComm439(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.,mjy)"
        cls.fname="C439_%s.fits"
        cls.setup2()

class TestComm440(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-15,photnu)"
        cls.fname="C440_%s.fits"
        cls.setup2()

class TestComm441(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-26,fnu)"
        cls.fname="C441_%s.fits"
        cls.setup2()

class TestComm442(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),1.e-3,jy)"
        cls.fname="C442_%s.fits"
        cls.setup2()

class TestComm443(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,abmag)"
        cls.fname="C443_%s.fits"
        cls.setup2()

class TestComm444(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(cos,nuv,g185m,c1835),16.0,stmag)"
        cls.fname="C444_%s.fits"
        cls.setup2()

class TestComm445(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.,mjy)"
        cls.fname="C445_%s.fits"
        cls.setup2()

class TestComm446(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.e-15,photnu)"
        cls.fname="C446_%s.fits"
        cls.setup2()

class TestComm447(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.e-26,fnu)"
        cls.fname="C447_%s.fits"
        cls.setup2()

class TestComm448(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),1.e-3,jy)"
        cls.fname="C448_%s.fits"
        cls.setup2()

class TestComm449(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),16.0,abmag)"
        cls.fname="C449_%s.fits"
        cls.setup2()

class TestComm450(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,fuv),16.0,stmag)"
        cls.fname="C450_%s.fits"
        cls.setup2()

class TestComm451(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.,mjy)"
        cls.fname="C451_%s.fits"
        cls.setup2()

class TestComm452(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.e-15,photnu)"
        cls.fname="C452_%s.fits"
        cls.setup2()

class TestComm453(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.e-26,fnu)"
        cls.fname="C453_%s.fits"
        cls.setup2()

class TestComm454(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),1.e-3,jy)"
        cls.fname="C454_%s.fits"
        cls.setup2()

class TestComm455(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),16.0,abmag)"
        cls.fname="C455_%s.fits"
        cls.setup2()

class TestComm456(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(icat(k93models,37000,0.0,4.0),band(galex,nuv),16.0,stmag)"
        cls.fname="C456_%s.fits"
        cls.setup2()

class TestComm457(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,1.0),band(nicmos,2,f205w),20,mjy)"
        cls.fname="C457_%s.fits"
        cls.setup2()

class TestComm458(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,1.5),band(nicmos,2,f237m),100000,counts)"
        cls.fname="C458_%s.fits"
        cls.setup2()

class TestComm459(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,h),1.0e-14,photnu)"
        cls.fname="C459_%s.fits"
        cls.setup2()

class TestComm460(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,h),1.0e-26,fnu)"
        cls.fname="C460_%s.fits"
        cls.setup2()

class TestComm461(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(bessell,k),5,obmag)"
        cls.fname="C461_%s.fits"
        cls.setup2()

class TestComm462(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(nicmos,2,f237m),0.5,jy)"
        cls.fname="C462_%s.fits"
        cls.setup2()

class TestComm463(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,2.0),band(nicmos,2,f237m),1.0e-4,photlam)"
        cls.fname="C463_%s.fits"
        cls.setup2()

class TestComm464(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="rn(z(crgridkc96$sb_template.fits,2.5),band(nicmos,3,f215n),20,mjy)"
        cls.fname="C464_%s.fits"
        cls.setup2()

class TestComm465(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        cls.fname="C465_%s.fits"
        cls.setup2()

class TestComm466(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits)"
        cls.fname="C466_%s.fits"
        cls.setup2()

class TestComm467(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits)"
        cls.fname="C467_%s.fits"
        cls.setup2()

class TestComm468(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits)"
        cls.fname="C468_%s.fits"
        cls.setup2()

class TestComm469(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits)"
        cls.fname="C469_%s.fits"
        cls.setup2()

class TestComm470(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits)"
        cls.fname="C470_%s.fits"
        cls.setup2()

class TestComm471(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="None"
        cls.spectrum="spec(egal.dat)"
        cls.fname="C471_%s.fits"
        cls.setup2()

class TestComm472(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C472_%s.fits"
        cls.setup2()

class TestComm473(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        cls.fname="C473_%s.fits"
        cls.setup2()

class TestComm474(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C474_%s.fits"
        cls.setup2()

class TestComm475(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        cls.fname="C475_%s.fits"
        cls.setup2()

class TestComm476(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        cls.fname="C476_%s.fits"
        cls.setup2()

class TestComm477(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.25"
        cls.fname="C477_%s.fits"
        cls.setup2()

class TestComm478(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*2.0"
        cls.fname="C478_%s.fits"
        cls.setup2()

class TestComm479(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,coron,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*4.0"
        cls.fname="C479_%s.fits"
        cls.setup2()

class TestComm480(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C480_%s.fits"
        cls.setup2()

class TestComm481(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C481_%s.fits"
        cls.setup2()

class TestComm482(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C482_%s.fits"
        cls.setup2()

class TestComm483(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C483_%s.fits"
        cls.setup2()

class TestComm484(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C484_%s.fits"
        cls.setup2()

class TestComm485(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f220w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C485_%s.fits"
        cls.setup2()

class TestComm486(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C486_%s.fits"
        cls.setup2()

class TestComm487(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C487_%s.fits"
        cls.setup2()

class TestComm488(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C488_%s.fits"
        cls.setup2()

class TestComm489(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C489_%s.fits"
        cls.setup2()

class TestComm490(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C490_%s.fits"
        cls.setup2()

class TestComm491(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f250w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C491_%s.fits"
        cls.setup2()

class TestComm492(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C492_%s.fits"
        cls.setup2()

class TestComm493(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C493_%s.fits"
        cls.setup2()

class TestComm494(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C494_%s.fits"
        cls.setup2()

class TestComm495(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.0e-17,flam)"
        cls.fname="C495_%s.fits"
        cls.setup2()

class TestComm496(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C496_%s.fits"
        cls.setup2()

class TestComm497(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C497_%s.fits"
        cls.setup2()

class TestComm498(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f330w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C498_%s.fits"
        cls.setup2()

class TestComm499(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C499_%s.fits"
        cls.setup2()

class TestComm500(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C500_%s.fits"
        cls.setup2()

class TestComm501(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C501_%s.fits"
        cls.setup2()

class TestComm502(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C502_%s.fits"
        cls.setup2()

class TestComm503(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f344n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C503_%s.fits"
        cls.setup2()

class TestComm504(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C504_%s.fits"
        cls.setup2()

class TestComm505(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C505_%s.fits"
        cls.setup2()

class TestComm506(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C506_%s.fits"
        cls.setup2()

class TestComm507(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C507_%s.fits"
        cls.setup2()

class TestComm508(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C508_%s.fits"
        cls.setup2()

class TestComm509(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f435w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C509_%s.fits"
        cls.setup2()

class TestComm510(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C510_%s.fits"
        cls.setup2()

class TestComm511(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C511_%s.fits"
        cls.setup2()

class TestComm512(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C512_%s.fits"
        cls.setup2()

class TestComm513(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C513_%s.fits"
        cls.setup2()

class TestComm514(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C514_%s.fits"
        cls.setup2()

class TestComm515(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C515_%s.fits"
        cls.setup2()

class TestComm516(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C516_%s.fits"
        cls.setup2()

class TestComm517(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C517_%s.fits"
        cls.setup2()

class TestComm518(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C518_%s.fits"
        cls.setup2()

class TestComm519(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C519_%s.fits"
        cls.setup2()

class TestComm520(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C520_%s.fits"
        cls.setup2()

class TestComm521(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C521_%s.fits"
        cls.setup2()

class TestComm522(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C522_%s.fits"
        cls.setup2()

class TestComm523(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C523_%s.fits"
        cls.setup2()

class TestComm524(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f550m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C524_%s.fits"
        cls.setup2()

class TestComm525(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C525_%s.fits"
        cls.setup2()

class TestComm526(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C526_%s.fits"
        cls.setup2()

class TestComm527(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C527_%s.fits"
        cls.setup2()

class TestComm528(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C528_%s.fits"
        cls.setup2()

class TestComm529(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C529_%s.fits"
        cls.setup2()

class TestComm530(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C530_%s.fits"
        cls.setup2()

class TestComm531(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C531_%s.fits"
        cls.setup2()

class TestComm532(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C532_%s.fits"
        cls.setup2()

class TestComm533(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C533_%s.fits"
        cls.setup2()

class TestComm534(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C534_%s.fits"
        cls.setup2()

class TestComm535(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),0,vegamag)"
        cls.fname="C535_%s.fits"
        cls.setup2()

class TestComm536(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),10,vegamag)"
        cls.fname="C536_%s.fits"
        cls.setup2()

class TestComm537(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C537_%s.fits"
        cls.setup2()

class TestComm538(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),5,vegamag)"
        cls.fname="C538_%s.fits"
        cls.setup2()

class TestComm539(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f555w,coron"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C539_%s.fits"
        cls.setup2()

class TestComm540(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C540_%s.fits"
        cls.setup2()

class TestComm541(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C541_%s.fits"
        cls.setup2()

class TestComm542(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C542_%s.fits"
        cls.setup2()

class TestComm543(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C543_%s.fits"
        cls.setup2()

class TestComm544(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C544_%s.fits"
        cls.setup2()

class TestComm545(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C545_%s.fits"
        cls.setup2()

class TestComm546(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C546_%s.fits"
        cls.setup2()

class TestComm547(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C547_%s.fits"
        cls.setup2()

class TestComm548(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C548_%s.fits"
        cls.setup2()

class TestComm549(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C549_%s.fits"
        cls.setup2()

class TestComm550(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C550_%s.fits"
        cls.setup2()

class TestComm551(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C551_%s.fits"
        cls.setup2()

class TestComm552(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C552_%s.fits"
        cls.setup2()

class TestComm553(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C553_%s.fits"
        cls.setup2()

class TestComm554(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C554_%s.fits"
        cls.setup2()

class TestComm555(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C555_%s.fits"
        cls.setup2()

class TestComm556(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C556_%s.fits"
        cls.setup2()

class TestComm557(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f660n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C557_%s.fits"
        cls.setup2()

class TestComm558(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C558_%s.fits"
        cls.setup2()

class TestComm559(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C559_%s.fits"
        cls.setup2()

class TestComm560(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C560_%s.fits"
        cls.setup2()

class TestComm561(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C561_%s.fits"
        cls.setup2()

class TestComm562(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C562_%s.fits"
        cls.setup2()

class TestComm563(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C563_%s.fits"
        cls.setup2()

class TestComm564(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C564_%s.fits"
        cls.setup2()

class TestComm565(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C565_%s.fits"
        cls.setup2()

class TestComm566(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C566_%s.fits"
        cls.setup2()

class TestComm567(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f814w"
        cls.spectrum="crcalspec$g191b2b_mod_004.fits"
        cls.fname="C567_%s.fits"
        cls.setup2()

class TestComm568(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C568_%s.fits"
        cls.setup2()

class TestComm569(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C569_%s.fits"
        cls.setup2()

class TestComm570(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C570_%s.fits"
        cls.setup2()

class TestComm571(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C571_%s.fits"
        cls.setup2()

class TestComm572(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C572_%s.fits"
        cls.setup2()

class TestComm573(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C573_%s.fits"
        cls.setup2()

class TestComm574(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C574_%s.fits"
        cls.setup2()

class TestComm575(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C575_%s.fits"
        cls.setup2()

class TestComm576(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C576_%s.fits"
        cls.setup2()

class TestComm577(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,f892n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C577_%s.fits"
        cls.setup2()

class TestComm578(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C578_%s.fits"
        cls.setup2()

class TestComm579(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        cls.fname="C579_%s.fits"
        cls.setup2()

class TestComm580(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        cls.fname="C580_%s.fits"
        cls.setup2()

class TestComm581(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        cls.fname="C581_%s.fits"
        cls.setup2()

class TestComm582(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        cls.fname="C582_%s.fits"
        cls.setup2()

class TestComm583(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        cls.fname="C583_%s.fits"
        cls.setup2()

class TestComm584(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C584_%s.fits"
        cls.setup2()

class TestComm585(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C585_%s.fits"
        cls.setup2()

class TestComm586(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C586_%s.fits"
        cls.setup2()

class TestComm587(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        cls.fname="C587_%s.fits"
        cls.setup2()

class TestComm588(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C588_%s.fits"
        cls.setup2()

class TestComm589(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C589_%s.fits"
        cls.setup2()

class TestComm590(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C590_%s.fits"
        cls.setup2()

class TestComm591(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C591_%s.fits"
        cls.setup2()

class TestComm592(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C592_%s.fits"
        cls.setup2()

class TestComm593(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C593_%s.fits"
        cls.setup2()

class TestComm594(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4590"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C594_%s.fits"
        cls.setup2()

class TestComm595(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4592"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C595_%s.fits"
        cls.setup2()

class TestComm596(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr459m#4592"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C596_%s.fits"
        cls.setup2()

class TestComm597(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr505n#5050"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C597_%s.fits"
        cls.setup2()

class TestComm598(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr505n#5050"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C598_%s.fits"
        cls.setup2()

class TestComm599(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr656n#6560"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C599_%s.fits"
        cls.setup2()

class TestComm600(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,fr656n#6560"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C600_%s.fits"
        cls.setup2()

class TestComm601(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        cls.fname="C601_%s.fits"
        cls.setup2()

class TestComm602(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C602_%s.fits"
        cls.setup2()

class TestComm603(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C603_%s.fits"
        cls.setup2()

class TestComm604(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C604_%s.fits"
        cls.setup2()

class TestComm605(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C605_%s.fits"
        cls.setup2()

class TestComm606(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C606_%s.fits"
        cls.setup2()

class TestComm607(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C607_%s.fits"
        cls.setup2()

class TestComm608(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C608_%s.fits"
        cls.setup2()

class TestComm609(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C609_%s.fits"
        cls.setup2()

class TestComm610(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="em(4000.0,10.0,1.0E-16,flam)"
        cls.fname="C610_%s.fits"
        cls.setup2()

class TestComm611(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C611_%s.fits"
        cls.setup2()

class TestComm612(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C612_%s.fits"
        cls.setup2()

class TestComm613(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C613_%s.fits"
        cls.setup2()

class TestComm614(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C614_%s.fits"
        cls.setup2()

class TestComm615(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C615_%s.fits"
        cls.setup2()

class TestComm616(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C616_%s.fits"
        cls.setup2()

class TestComm617(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C617_%s.fits"
        cls.setup2()

class TestComm618(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,hrc,pr200l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C618_%s.fits"
        cls.setup2()

class TestComm619(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C619_%s.fits"
        cls.setup2()

class TestComm620(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C620_%s.fits"
        cls.setup2()

class TestComm621(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C621_%s.fits"
        cls.setup2()

class TestComm622(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C622_%s.fits"
        cls.setup2()

class TestComm623(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f115lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C623_%s.fits"
        cls.setup2()

class TestComm624(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f122m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C624_%s.fits"
        cls.setup2()

class TestComm625(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f122m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C625_%s.fits"
        cls.setup2()

class TestComm626(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C626_%s.fits"
        cls.setup2()

class TestComm627(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-17,flam)"
        cls.fname="C627_%s.fits"
        cls.setup2()

class TestComm628(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f125lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C628_%s.fits"
        cls.setup2()

class TestComm629(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f140lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C629_%s.fits"
        cls.setup2()

class TestComm630(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f140lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C630_%s.fits"
        cls.setup2()

class TestComm631(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(bb(10000),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C631_%s.fits"
        cls.setup2()

class TestComm632(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C632_%s.fits"
        cls.setup2()

class TestComm633(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C633_%s.fits"
        cls.setup2()

class TestComm634(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C634_%s.fits"
        cls.setup2()

class TestComm635(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C635_%s.fits"
        cls.setup2()

class TestComm636(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f150lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C636_%s.fits"
        cls.setup2()

class TestComm637(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f165lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C637_%s.fits"
        cls.setup2()

class TestComm638(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,f165lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C638_%s.fits"
        cls.setup2()

class TestComm639(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        cls.fname="C639_%s.fits"
        cls.setup2()

class TestComm640(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C640_%s.fits"
        cls.setup2()

class TestComm641(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C641_%s.fits"
        cls.setup2()

class TestComm642(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C642_%s.fits"
        cls.setup2()

class TestComm643(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C643_%s.fits"
        cls.setup2()

class TestComm644(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C644_%s.fits"
        cls.setup2()

class TestComm645(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C645_%s.fits"
        cls.setup2()

class TestComm646(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C646_%s.fits"
        cls.setup2()

class TestComm647(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C647_%s.fits"
        cls.setup2()

class TestComm648(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr110l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C648_%s.fits"
        cls.setup2()

class TestComm649(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="em(1400.0,10.0,1.0E-16,flam)"
        cls.fname="C649_%s.fits"
        cls.setup2()

class TestComm650(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C650_%s.fits"
        cls.setup2()

class TestComm651(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C651_%s.fits"
        cls.setup2()

class TestComm652(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C652_%s.fits"
        cls.setup2()

class TestComm653(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C653_%s.fits"
        cls.setup2()

class TestComm654(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C654_%s.fits"
        cls.setup2()

class TestComm655(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C655_%s.fits"
        cls.setup2()

class TestComm656(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C656_%s.fits"
        cls.setup2()

class TestComm657(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,sbc,pr130l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C657_%s.fits"
        cls.setup2()

class TestComm658(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C658_%s.fits"
        cls.setup2()

class TestComm659(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C659_%s.fits"
        cls.setup2()

class TestComm660(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C660_%s.fits"
        cls.setup2()

class TestComm661(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C661_%s.fits"
        cls.setup2()

class TestComm662(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f435w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C662_%s.fits"
        cls.setup2()

class TestComm663(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C663_%s.fits"
        cls.setup2()

class TestComm664(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C664_%s.fits"
        cls.setup2()

class TestComm665(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C665_%s.fits"
        cls.setup2()

class TestComm666(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C666_%s.fits"
        cls.setup2()

class TestComm667(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C667_%s.fits"
        cls.setup2()

class TestComm668(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C668_%s.fits"
        cls.setup2()

class TestComm669(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C669_%s.fits"
        cls.setup2()

class TestComm670(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C670_%s.fits"
        cls.setup2()

class TestComm671(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C671_%s.fits"
        cls.setup2()

class TestComm672(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C672_%s.fits"
        cls.setup2()

class TestComm673(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C673_%s.fits"
        cls.setup2()

class TestComm674(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C674_%s.fits"
        cls.setup2()

class TestComm675(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C675_%s.fits"
        cls.setup2()

class TestComm676(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C676_%s.fits"
        cls.setup2()

class TestComm677(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f550m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C677_%s.fits"
        cls.setup2()

class TestComm678(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C678_%s.fits"
        cls.setup2()

class TestComm679(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C679_%s.fits"
        cls.setup2()

class TestComm680(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C680_%s.fits"
        cls.setup2()

class TestComm681(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C681_%s.fits"
        cls.setup2()

class TestComm682(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C682_%s.fits"
        cls.setup2()

class TestComm683(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C683_%s.fits"
        cls.setup2()

class TestComm684(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C684_%s.fits"
        cls.setup2()

class TestComm685(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C685_%s.fits"
        cls.setup2()

class TestComm686(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C686_%s.fits"
        cls.setup2()

class TestComm687(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C687_%s.fits"
        cls.setup2()

class TestComm688(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C688_%s.fits"
        cls.setup2()

class TestComm689(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C689_%s.fits"
        cls.setup2()

class TestComm690(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w,pol_v"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C690_%s.fits"
        cls.setup2()

class TestComm691(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f555w,pol_v"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C691_%s.fits"
        cls.setup2()

class TestComm692(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C692_%s.fits"
        cls.setup2()

class TestComm693(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C693_%s.fits"
        cls.setup2()

class TestComm694(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C694_%s.fits"
        cls.setup2()

class TestComm695(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C695_%s.fits"
        cls.setup2()

class TestComm696(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C696_%s.fits"
        cls.setup2()

class TestComm697(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C697_%s.fits"
        cls.setup2()

class TestComm698(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C698_%s.fits"
        cls.setup2()

class TestComm699(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C699_%s.fits"
        cls.setup2()

class TestComm700(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C700_%s.fits"
        cls.setup2()

class TestComm701(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C701_%s.fits"
        cls.setup2()

class TestComm702(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C702_%s.fits"
        cls.setup2()

class TestComm703(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C703_%s.fits"
        cls.setup2()

class TestComm704(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C704_%s.fits"
        cls.setup2()

class TestComm705(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C705_%s.fits"
        cls.setup2()

class TestComm706(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C706_%s.fits"
        cls.setup2()

class TestComm707(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C707_%s.fits"
        cls.setup2()

class TestComm708(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C708_%s.fits"
        cls.setup2()

class TestComm709(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C709_%s.fits"
        cls.setup2()

class TestComm710(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C710_%s.fits"
        cls.setup2()

class TestComm711(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C711_%s.fits"
        cls.setup2()

class TestComm712(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f660n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C712_%s.fits"
        cls.setup2()

class TestComm713(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C713_%s.fits"
        cls.setup2()

class TestComm714(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C714_%s.fits"
        cls.setup2()

class TestComm715(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C715_%s.fits"
        cls.setup2()

class TestComm716(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C716_%s.fits"
        cls.setup2()

class TestComm717(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C717_%s.fits"
        cls.setup2()

class TestComm718(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C718_%s.fits"
        cls.setup2()

class TestComm719(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C719_%s.fits"
        cls.setup2()

class TestComm720(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C720_%s.fits"
        cls.setup2()

class TestComm721(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C721_%s.fits"
        cls.setup2()

class TestComm722(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C722_%s.fits"
        cls.setup2()

class TestComm723(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C723_%s.fits"
        cls.setup2()

class TestComm724(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C724_%s.fits"
        cls.setup2()

class TestComm725(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C725_%s.fits"
        cls.setup2()

class TestComm726(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C726_%s.fits"
        cls.setup2()

class TestComm727(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C727_%s.fits"
        cls.setup2()

class TestComm728(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C728_%s.fits"
        cls.setup2()

class TestComm729(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C729_%s.fits"
        cls.setup2()

class TestComm730(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C730_%s.fits"
        cls.setup2()

class TestComm731(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C731_%s.fits"
        cls.setup2()

class TestComm732(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1e-18,flam)"
        cls.fname="C732_%s.fits"
        cls.setup2()

class TestComm733(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,f892n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C733_%s.fits"
        cls.setup2()

class TestComm734(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr1016n#10000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C734_%s.fits"
        cls.setup2()

class TestComm735(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr1016n#10000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C735_%s.fits"
        cls.setup2()

class TestComm736(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="em(3880.0,10.0,1.0E-16,flam)"
        cls.fname="C736_%s.fits"
        cls.setup2()

class TestComm737(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C737_%s.fits"
        cls.setup2()

class TestComm738(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9),band(johnson,v),15,vegamag)"
        cls.fname="C738_%s.fits"
        cls.setup2()

class TestComm739(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6),band(johnson,v),15,vegamag)"
        cls.fname="C739_%s.fits"
        cls.setup2()

class TestComm740(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),15,vegamag)"
        cls.fname="C740_%s.fits"
        cls.setup2()

class TestComm741(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),band(johnson,v),15,vegamag)"
        cls.fname="C741_%s.fits"
        cls.setup2()

class TestComm742(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),15,vegamag)"
        cls.fname="C742_%s.fits"
        cls.setup2()

class TestComm743(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C743_%s.fits"
        cls.setup2()

class TestComm744(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C744_%s.fits"
        cls.setup2()

class TestComm745(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C745_%s.fits"
        cls.setup2()

class TestComm746(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C746_%s.fits"
        cls.setup2()

class TestComm747(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.E-15,flam)"
        cls.fname="C747_%s.fits"
        cls.setup2()

class TestComm748(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C748_%s.fits"
        cls.setup2()

class TestComm749(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C749_%s.fits"
        cls.setup2()

class TestComm750(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C750_%s.fits"
        cls.setup2()

class TestComm751(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3880"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C751_%s.fits"
        cls.setup2()

class TestComm752(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3881"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C752_%s.fits"
        cls.setup2()

class TestComm753(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr388n#3881"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C753_%s.fits"
        cls.setup2()

class TestComm754(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr423n#4230"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C754_%s.fits"
        cls.setup2()

class TestComm755(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr423n#4230"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C755_%s.fits"
        cls.setup2()

class TestComm756(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4590"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),22,vegamag)"
        cls.fname="C756_%s.fits"
        cls.setup2()

class TestComm757(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4590"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C757_%s.fits"
        cls.setup2()

class TestComm758(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4620"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C758_%s.fits"
        cls.setup2()

class TestComm759(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr459m#4620"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C759_%s.fits"
        cls.setup2()

class TestComm760(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr462n#4620"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C760_%s.fits"
        cls.setup2()

class TestComm761(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr462n#4620"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C761_%s.fits"
        cls.setup2()

class TestComm762(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr505n#5000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C762_%s.fits"
        cls.setup2()

class TestComm763(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr505n#5000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C763_%s.fits"
        cls.setup2()

class TestComm764(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr551n#5500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C764_%s.fits"
        cls.setup2()

class TestComm765(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr551n#5500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C765_%s.fits"
        cls.setup2()

class TestComm766(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr601n#6000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C766_%s.fits"
        cls.setup2()

class TestComm767(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr601n#6000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C767_%s.fits"
        cls.setup2()

class TestComm768(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr647m#6470"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C768_%s.fits"
        cls.setup2()

class TestComm769(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr647m#6470"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C769_%s.fits"
        cls.setup2()

class TestComm770(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr656n#6500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C770_%s.fits"
        cls.setup2()

class TestComm771(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr656n#6500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C771_%s.fits"
        cls.setup2()

class TestComm772(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr716n#7100"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C772_%s.fits"
        cls.setup2()

class TestComm773(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr716n#7100"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C773_%s.fits"
        cls.setup2()

class TestComm774(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr782n#7900"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C774_%s.fits"
        cls.setup2()

class TestComm775(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr782n#7900"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C775_%s.fits"
        cls.setup2()

class TestComm776(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr853n#8500"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C776_%s.fits"
        cls.setup2()

class TestComm777(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr853n#8500"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C777_%s.fits"
        cls.setup2()

class TestComm778(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr914m#9000"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C778_%s.fits"
        cls.setup2()

class TestComm779(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr914m#9000"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C779_%s.fits"
        cls.setup2()

class TestComm780(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr931n#9300"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.e-15,flam)"
        cls.fname="C780_%s.fits"
        cls.setup2()

class TestComm781(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,fr931n#9300"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C781_%s.fits"
        cls.setup2()

class TestComm782(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="em(6500.0,10.0,1.0E-16,flam)"
        cls.fname="C782_%s.fits"
        cls.setup2()

class TestComm783(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(bb(10000),band(johnson,v),20,vegamag)"
        cls.fname="C783_%s.fits"
        cls.setup2()

class TestComm784(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),20,vegamag)"
        cls.fname="C784_%s.fits"
        cls.setup2()

class TestComm785(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C785_%s.fits"
        cls.setup2()

class TestComm786(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C786_%s.fits"
        cls.setup2()

class TestComm787(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="rn(unit(1.0,flam),box(5500.0,1.0),1.5e-16,flam)"
        cls.fname="C787_%s.fits"
        cls.setup2()

class TestComm788(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C788_%s.fits"
        cls.setup2()

class TestComm789(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C789_%s.fits"
        cls.setup2()

class TestComm790(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="acs,wfc1,g800l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C790_%s.fits"
        cls.setup2()

class TestComm791(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="None"
        cls.fname="C791_%s.fits"
        cls.setup2()

class TestComm792(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C792_%s.fits"
        cls.setup2()

class TestComm793(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C793_%s.fits"
        cls.setup2()

class TestComm794(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C794_%s.fits"
        cls.setup2()

class TestComm795(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f090m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C795_%s.fits"
        cls.setup2()

class TestComm796(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="None"
        cls.fname="C796_%s.fits"
        cls.setup2()

class TestComm797(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C797_%s.fits"
        cls.setup2()

class TestComm798(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f095n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C798_%s.fits"
        cls.setup2()

class TestComm799(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="None"
        cls.fname="C799_%s.fits"
        cls.setup2()

class TestComm800(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C800_%s.fits"
        cls.setup2()

class TestComm801(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f097n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C801_%s.fits"
        cls.setup2()

class TestComm802(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="None"
        cls.fname="C802_%s.fits"
        cls.setup2()

class TestComm803(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C803_%s.fits"
        cls.setup2()

class TestComm804(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f108n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C804_%s.fits"
        cls.setup2()

class TestComm805(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="None"
        cls.fname="C805_%s.fits"
        cls.setup2()

class TestComm806(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C806_%s.fits"
        cls.setup2()

class TestComm807(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C807_%s.fits"
        cls.setup2()

class TestComm808(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="None"
        cls.fname="C808_%s.fits"
        cls.setup2()

class TestComm809(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="em(10000.0,10.0,1.0E-13,flam)"
        cls.fname="C809_%s.fits"
        cls.setup2()

class TestComm810(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(10000),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C810_%s.fits"
        cls.setup2()

class TestComm811(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C811_%s.fits"
        cls.setup2()

class TestComm812(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5000),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C812_%s.fits"
        cls.setup2()

class TestComm813(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C813_%s.fits"
        cls.setup2()

class TestComm814(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C814_%s.fits"
        cls.setup2()

class TestComm815(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(6200),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C815_%s.fits"
        cls.setup2()

class TestComm816(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(bb(7700),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C816_%s.fits"
        cls.setup2()

class TestComm817(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,15000,0.0,3.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C817_%s.fits"
        cls.setup2()

class TestComm818(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,4750,0.0,1.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C818_%s.fits"
        cls.setup2()

class TestComm819(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,6250,0.0,4.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C819_%s.fits"
        cls.setup2()

class TestComm820(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(ck04models,7750,0.0,2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C820_%s.fits"
        cls.setup2()

class TestComm821(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C821_%s.fits"
        cls.setup2()

class TestComm822(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C822_%s.fits"
        cls.setup2()

class TestComm823(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C823_%s.fits"
        cls.setup2()

class TestComm824(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-0.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C824_%s.fits"
        cls.setup2()

class TestComm825(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C825_%s.fits"
        cls.setup2()

class TestComm826(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(pl(4000.0,-1.5,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C826_%s.fits"
        cls.setup2()

class TestComm827(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C827_%s.fits"
        cls.setup2()

class TestComm828(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C828_%s.fits"
        cls.setup2()

class TestComm829(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C829_%s.fits"
        cls.setup2()

class TestComm830(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/bpgs/bpgs_35.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C830_%s.fits"
        cls.setup2()

class TestComm831(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_121.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C831_%s.fits"
        cls.setup2()

class TestComm832(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_126.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C832_%s.fits"
        cls.setup2()

class TestComm833(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_127.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C833_%s.fits"
        cls.setup2()

class TestComm834(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C834_%s.fits"
        cls.setup2()

class TestComm835(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C835_%s.fits"
        cls.setup2()

class TestComm836(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C836_%s.fits"
        cls.setup2()

class TestComm837(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(earthshine.fits),band(johnson,v),28.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C837_%s.fits"
        cls.setup2()

class TestComm838(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(earthshine.fits),band(johnson,v),30.0,vegamag)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C838_%s.fits"
        cls.setup2()

class TestComm839(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(egal.dat),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C839_%s.fits"
        cls.setup2()

class TestComm840(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(spec(spiral.fits),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C840_%s.fits"
        cls.setup2()

class TestComm841(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal1),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C841_%s.fits"
        cls.setup2()

class TestComm842(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,gal3),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C842_%s.fits"
        cls.setup2()

class TestComm843(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,lmc),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C843_%s.fits"
        cls.setup2()

class TestComm844(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam)*ebmvx(3.0,xgal),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C844_%s.fits"
        cls.setup2()

class TestComm845(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,k),15,vegamag)"
        cls.fname="C845_%s.fits"
        cls.setup2()

class TestComm846(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,k),20,vegamag)"
        cls.fname="C846_%s.fits"
        cls.setup2()

class TestComm847(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(cousins,i),15,vegamag)"
        cls.fname="C847_%s.fits"
        cls.setup2()

class TestComm848(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,k),15,vegamag)"
        cls.fname="C848_%s.fits"
        cls.setup2()

class TestComm849(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,k),20,vegamag)"
        cls.fname="C849_%s.fits"
        cls.setup2()

class TestComm850(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C850_%s.fits"
        cls.setup2()

class TestComm851(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),20,vegamag)"
        cls.fname="C851_%s.fits"
        cls.setup2()

class TestComm852(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C852_%s.fits"
        cls.setup2()

class TestComm853(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f160w),15,vegamag)"
        cls.fname="C853_%s.fits"
        cls.setup2()

class TestComm854(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),15,vegamag)"
        cls.fname="C854_%s.fits"
        cls.setup2()

class TestComm855(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-06,jy)"
        cls.fname="C855_%s.fits"
        cls.setup2()

class TestComm856(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C856_%s.fits"
        cls.setup2()

class TestComm857(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal1)"
        cls.fname="C857_%s.fits"
        cls.setup2()

class TestComm858(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,gal3)"
        cls.fname="C858_%s.fits"
        cls.setup2()

class TestComm859(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,lmc)"
        cls.fname="C859_%s.fits"
        cls.setup2()

class TestComm860(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)*ebmvx(3.0,xgal)"
        cls.fname="C860_%s.fits"
        cls.setup2()

class TestComm861(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(10000.0,1.0),1.00E-13,flam)+em(10000.0,10.0,1.0E-13,flam)"
        cls.fname="C861_%s.fits"
        cls.setup2()

class TestComm862(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-06,jy)"
        cls.fname="C862_%s.fits"
        cls.setup2()

class TestComm863(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(15999.999999999998,1.0),1.00E-13,flam)"
        cls.fname="C863_%s.fits"
        cls.setup2()

class TestComm864(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-06,jy)"
        cls.fname="C864_%s.fits"
        cls.setup2()

class TestComm865(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,flam),box(22000.0,1.0),1.00E-13,flam)"
        cls.fname="C865_%s.fits"
        cls.setup2()

class TestComm866(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(unit(1.0,fnu),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C866_%s.fits"
        cls.setup2()

class TestComm867(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.5),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C867_%s.fits"
        cls.setup2()

class TestComm868(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),1.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C868_%s.fits"
        cls.setup2()

class TestComm869(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C869_%s.fits"
        cls.setup2()

class TestComm870(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="rn(z(spec(qso_template.fits),2.0),box(10000.0,1.0),1.00E-13,flam)"
        cls.fname="C870_%s.fits"
        cls.setup2()

class TestComm871(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/1740346_nic_001.fits)"
        cls.fname="C871_%s.fits"
        cls.setup2()

class TestComm872(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C872_%s.fits"
        cls.setup2()

class TestComm873(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C873_%s.fits"
        cls.setup2()

class TestComm874(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C874_%s.fits"
        cls.setup2()

class TestComm875(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.628378447488586,vegamag)"
        cls.fname="C875_%s.fits"
        cls.setup2()

class TestComm876(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.0086,vegamag)"
        cls.fname="C876_%s.fits"
        cls.setup2()

class TestComm877(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C877_%s.fits"
        cls.setup2()

class TestComm878(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.26738684931507,vegamag)"
        cls.fname="C878_%s.fits"
        cls.setup2()

class TestComm879(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.40573333333333,vegamag)"
        cls.fname="C879_%s.fits"
        cls.setup2()

class TestComm880(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C880_%s.fits"
        cls.setup2()

class TestComm881(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.808112328767123,vegamag)"
        cls.fname="C881_%s.fits"
        cls.setup2()

class TestComm882(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.9514,vegamag)"
        cls.fname="C882_%s.fits"
        cls.setup2()

class TestComm883(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.964448767123287,vegamag)"
        cls.fname="C883_%s.fits"
        cls.setup2()

class TestComm884(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.067600000000002,vegamag)"
        cls.fname="C884_%s.fits"
        cls.setup2()

class TestComm885(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.1514,vegamag)"
        cls.fname="C885_%s.fits"
        cls.setup2()

class TestComm886(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C886_%s.fits"
        cls.setup2()

class TestComm887(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),28.0,vegamag)"
        cls.fname="C887_%s.fits"
        cls.setup2()

class TestComm888(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),30.0,vegamag)"
        cls.fname="C888_%s.fits"
        cls.setup2()

class TestComm889(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.0"
        cls.fname="C889_%s.fits"
        cls.setup2()

class TestComm890(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*1.5"
        cls.fname="C890_%s.fits"
        cls.setup2()

class TestComm891(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*1.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C891_%s.fits"
        cls.setup2()

class TestComm892(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C892_%s.fits"
        cls.setup2()

class TestComm893(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f110w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C893_%s.fits"
        cls.setup2()

class TestComm894(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f113n"
        cls.spectrum="None"
        cls.fname="C894_%s.fits"
        cls.setup2()

class TestComm895(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f113n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C895_%s.fits"
        cls.setup2()

class TestComm896(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f113n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C896_%s.fits"
        cls.setup2()

class TestComm897(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f140w"
        cls.spectrum="None"
        cls.fname="C897_%s.fits"
        cls.setup2()

class TestComm898(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f140w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C898_%s.fits"
        cls.setup2()

class TestComm899(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f140w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C899_%s.fits"
        cls.setup2()

class TestComm900(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="None"
        cls.fname="C900_%s.fits"
        cls.setup2()

class TestComm901(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C901_%s.fits"
        cls.setup2()

class TestComm902(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f145m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C902_%s.fits"
        cls.setup2()

class TestComm903(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="None"
        cls.fname="C903_%s.fits"
        cls.setup2()

class TestComm904(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C904_%s.fits"
        cls.setup2()

class TestComm905(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C905_%s.fits"
        cls.setup2()

class TestComm906(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C906_%s.fits"
        cls.setup2()

class TestComm907(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C907_%s.fits"
        cls.setup2()

class TestComm908(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C908_%s.fits"
        cls.setup2()

class TestComm909(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C909_%s.fits"
        cls.setup2()

class TestComm910(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C910_%s.fits"
        cls.setup2()

class TestComm911(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="None"
        cls.fname="C911_%s.fits"
        cls.setup2()

class TestComm912(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C912_%s.fits"
        cls.setup2()

class TestComm913(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C913_%s.fits"
        cls.setup2()

class TestComm914(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="None"
        cls.fname="C914_%s.fits"
        cls.setup2()

class TestComm915(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C915_%s.fits"
        cls.setup2()

class TestComm916(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C916_%s.fits"
        cls.setup2()

class TestComm917(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f165m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C917_%s.fits"
        cls.setup2()

class TestComm918(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="None"
        cls.fname="C918_%s.fits"
        cls.setup2()

class TestComm919(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C919_%s.fits"
        cls.setup2()

class TestComm920(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f166n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C920_%s.fits"
        cls.setup2()

class TestComm921(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="None"
        cls.fname="C921_%s.fits"
        cls.setup2()

class TestComm922(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C922_%s.fits"
        cls.setup2()

class TestComm923(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f170m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C923_%s.fits"
        cls.setup2()

class TestComm924(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="None"
        cls.fname="C924_%s.fits"
        cls.setup2()

class TestComm925(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C925_%s.fits"
        cls.setup2()

class TestComm926(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C926_%s.fits"
        cls.setup2()

class TestComm927(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="None"
        cls.fname="C927_%s.fits"
        cls.setup2()

class TestComm928(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C928_%s.fits"
        cls.setup2()

class TestComm929(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C929_%s.fits"
        cls.setup2()

class TestComm930(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="None"
        cls.fname="C930_%s.fits"
        cls.setup2()

class TestComm931(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C931_%s.fits"
        cls.setup2()

class TestComm932(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,1,pol0s"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C932_%s.fits"
        cls.setup2()

class TestComm933(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="None"
        cls.fname="C933_%s.fits"
        cls.setup2()

class TestComm934(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C934_%s.fits"
        cls.setup2()

class TestComm935(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C935_%s.fits"
        cls.setup2()

class TestComm936(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C936_%s.fits"
        cls.setup2()

class TestComm937(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C937_%s.fits"
        cls.setup2()

class TestComm938(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C938_%s.fits"
        cls.setup2()

class TestComm939(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C939_%s.fits"
        cls.setup2()

class TestComm940(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C940_%s.fits"
        cls.setup2()

class TestComm941(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="None"
        cls.fname="C941_%s.fits"
        cls.setup2()

class TestComm942(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C942_%s.fits"
        cls.setup2()

class TestComm943(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C943_%s.fits"
        cls.setup2()

class TestComm944(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C944_%s.fits"
        cls.setup2()

class TestComm945(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C945_%s.fits"
        cls.setup2()

class TestComm946(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C946_%s.fits"
        cls.setup2()

class TestComm947(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C947_%s.fits"
        cls.setup2()

class TestComm948(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C948_%s.fits"
        cls.setup2()

class TestComm949(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="None"
        cls.fname="C949_%s.fits"
        cls.setup2()

class TestComm950(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C950_%s.fits"
        cls.setup2()

class TestComm951(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C951_%s.fits"
        cls.setup2()

class TestComm952(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C952_%s.fits"
        cls.setup2()

class TestComm953(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f165m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C953_%s.fits"
        cls.setup2()

class TestComm954(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="None"
        cls.fname="C954_%s.fits"
        cls.setup2()

class TestComm955(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C955_%s.fits"
        cls.setup2()

class TestComm956(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f171m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C956_%s.fits"
        cls.setup2()

class TestComm957(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="None"
        cls.fname="C957_%s.fits"
        cls.setup2()

class TestComm958(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C958_%s.fits"
        cls.setup2()

class TestComm959(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f180m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C959_%s.fits"
        cls.setup2()

class TestComm960(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="None"
        cls.fname="C960_%s.fits"
        cls.setup2()

class TestComm961(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C961_%s.fits"
        cls.setup2()

class TestComm962(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C962_%s.fits"
        cls.setup2()

class TestComm963(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187w"
        cls.spectrum="None"
        cls.fname="C963_%s.fits"
        cls.setup2()

class TestComm964(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C964_%s.fits"
        cls.setup2()

class TestComm965(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f187w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C965_%s.fits"
        cls.setup2()

class TestComm966(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f190n"
        cls.spectrum="None"
        cls.fname="C966_%s.fits"
        cls.setup2()

class TestComm967(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C967_%s.fits"
        cls.setup2()

class TestComm968(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C968_%s.fits"
        cls.setup2()

class TestComm969(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f204m"
        cls.spectrum="None"
        cls.fname="C969_%s.fits"
        cls.setup2()

class TestComm970(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f204m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C970_%s.fits"
        cls.setup2()

class TestComm971(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f204m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C971_%s.fits"
        cls.setup2()

class TestComm972(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f205w"
        cls.spectrum="None"
        cls.fname="C972_%s.fits"
        cls.setup2()

class TestComm973(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f205w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C973_%s.fits"
        cls.setup2()

class TestComm974(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f205w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C974_%s.fits"
        cls.setup2()

class TestComm975(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f207m"
        cls.spectrum="None"
        cls.fname="C975_%s.fits"
        cls.setup2()

class TestComm976(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f207m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C976_%s.fits"
        cls.setup2()

class TestComm977(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f207m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C977_%s.fits"
        cls.setup2()

class TestComm978(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f212n"
        cls.spectrum="None"
        cls.fname="C978_%s.fits"
        cls.setup2()

class TestComm979(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f212n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C979_%s.fits"
        cls.setup2()

class TestComm980(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f212n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C980_%s.fits"
        cls.setup2()

class TestComm981(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f216n"
        cls.spectrum="None"
        cls.fname="C981_%s.fits"
        cls.setup2()

class TestComm982(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f216n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C982_%s.fits"
        cls.setup2()

class TestComm983(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f216n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C983_%s.fits"
        cls.setup2()

class TestComm984(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="None"
        cls.fname="C984_%s.fits"
        cls.setup2()

class TestComm985(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C985_%s.fits"
        cls.setup2()

class TestComm986(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C986_%s.fits"
        cls.setup2()

class TestComm987(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C987_%s.fits"
        cls.setup2()

class TestComm988(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f222m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C988_%s.fits"
        cls.setup2()

class TestComm989(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f237m"
        cls.spectrum="None"
        cls.fname="C989_%s.fits"
        cls.setup2()

class TestComm990(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f237m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C990_%s.fits"
        cls.setup2()

class TestComm991(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,f237m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C991_%s.fits"
        cls.setup2()

class TestComm992(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,pol0l"
        cls.spectrum="None"
        cls.fname="C992_%s.fits"
        cls.setup2()

class TestComm993(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,pol0l"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C993_%s.fits"
        cls.setup2()

class TestComm994(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,2,pol0l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C994_%s.fits"
        cls.setup2()

class TestComm995(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f108n"
        cls.spectrum="None"
        cls.fname="C995_%s.fits"
        cls.setup2()

class TestComm996(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f108n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C996_%s.fits"
        cls.setup2()

class TestComm997(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f108n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C997_%s.fits"
        cls.setup2()

class TestComm998(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="None"
        cls.fname="C998_%s.fits"
        cls.setup2()

class TestComm999(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(10000),band(bessell,h),20,vegamag)"
        cls.fname="C999_%s.fits"
        cls.setup2()

class TestComm1000(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1000_%s.fits"
        cls.setup2()

class TestComm1001(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5500)*ebmvx(0.5,lmc),band(bessell,h),20,vegamag)"
        cls.fname="C1001_%s.fits"
        cls.setup2()

class TestComm1002(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1002_%s.fits"
        cls.setup2()

class TestComm1003(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1003_%s.fits"
        cls.setup2()

class TestComm1004(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(bessell,h),20,vegamag)"
        cls.fname="C1004_%s.fits"
        cls.setup2()

class TestComm1005(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(bessell,h),20,vegamag)"
        cls.fname="C1005_%s.fits"
        cls.setup2()

class TestComm1006(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(bessell,h),20,vegamag)"
        cls.fname="C1006_%s.fits"
        cls.setup2()

class TestComm1007(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(bessell,h),20,vegamag)"
        cls.fname="C1007_%s.fits"
        cls.setup2()

class TestComm1008(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(bessell,h),20,vegamag)"
        cls.fname="C1008_%s.fits"
        cls.setup2()

class TestComm1009(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(spec(egal.dat),band(bessell,h),20,vegamag)"
        cls.fname="C1009_%s.fits"
        cls.setup2()

class TestComm1010(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="rn(unit(1.0,flam),band(bessell,h),20,vegamag)"
        cls.fname="C1010_%s.fits"
        cls.setup2()

class TestComm1011(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1011_%s.fits"
        cls.setup2()

class TestComm1012(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f113n"
        cls.spectrum="None"
        cls.fname="C1012_%s.fits"
        cls.setup2()

class TestComm1013(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f113n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1013_%s.fits"
        cls.setup2()

class TestComm1014(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f113n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1014_%s.fits"
        cls.setup2()

class TestComm1015(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="None"
        cls.fname="C1015_%s.fits"
        cls.setup2()

class TestComm1016(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1016_%s.fits"
        cls.setup2()

class TestComm1017(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(bb(5500),band(bessell,h),23.5,vegamag)"
        cls.fname="C1017_%s.fits"
        cls.setup2()

class TestComm1018(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1018_%s.fits"
        cls.setup2()

class TestComm1019(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1019_%s.fits"
        cls.setup2()

class TestComm1020(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1020_%s.fits"
        cls.setup2()

class TestComm1021(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1021_%s.fits"
        cls.setup2()

class TestComm1022(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1022_%s.fits"
        cls.setup2()

class TestComm1023(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1023_%s.fits"
        cls.setup2()

class TestComm1024(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1024_%s.fits"
        cls.setup2()

class TestComm1025(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1025_%s.fits"
        cls.setup2()

class TestComm1026(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1026_%s.fits"
        cls.setup2()

class TestComm1027(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1027_%s.fits"
        cls.setup2()

class TestComm1028(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1028_%s.fits"
        cls.setup2()

class TestComm1029(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f150w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1029_%s.fits"
        cls.setup2()

class TestComm1030(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="None"
        cls.fname="C1030_%s.fits"
        cls.setup2()

class TestComm1031(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1031_%s.fits"
        cls.setup2()

class TestComm1032(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1032_%s.fits"
        cls.setup2()

class TestComm1033(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1033_%s.fits"
        cls.setup2()

class TestComm1034(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits)"
        cls.fname="C1034_%s.fits"
        cls.setup2()

class TestComm1035(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits)"
        cls.fname="C1035_%s.fits"
        cls.setup2()

class TestComm1036(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits)"
        cls.fname="C1036_%s.fits"
        cls.setup2()

class TestComm1037(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1037_%s.fits"
        cls.setup2()

class TestComm1038(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="None"
        cls.fname="C1038_%s.fits"
        cls.setup2()

class TestComm1039(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1039_%s.fits"
        cls.setup2()

class TestComm1040(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1040_%s.fits"
        cls.setup2()

class TestComm1041(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="None"
        cls.fname="C1041_%s.fits"
        cls.setup2()

class TestComm1042(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1042_%s.fits"
        cls.setup2()

class TestComm1043(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f166n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1043_%s.fits"
        cls.setup2()

class TestComm1044(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="None"
        cls.fname="C1044_%s.fits"
        cls.setup2()

class TestComm1045(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1045_%s.fits"
        cls.setup2()

class TestComm1046(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1046_%s.fits"
        cls.setup2()

class TestComm1047(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1047_%s.fits"
        cls.setup2()

class TestComm1048(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f175w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1048_%s.fits"
        cls.setup2()

class TestComm1049(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="None"
        cls.fname="C1049_%s.fits"
        cls.setup2()

class TestComm1050(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1050_%s.fits"
        cls.setup2()

class TestComm1051(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f187n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1051_%s.fits"
        cls.setup2()

class TestComm1052(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="None"
        cls.fname="C1052_%s.fits"
        cls.setup2()

class TestComm1053(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1053_%s.fits"
        cls.setup2()

class TestComm1054(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f190n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1054_%s.fits"
        cls.setup2()

class TestComm1055(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="None"
        cls.fname="C1055_%s.fits"
        cls.setup2()

class TestComm1056(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1056_%s.fits"
        cls.setup2()

class TestComm1057(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f196n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1057_%s.fits"
        cls.setup2()

class TestComm1058(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="None"
        cls.fname="C1058_%s.fits"
        cls.setup2()

class TestComm1059(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1059_%s.fits"
        cls.setup2()

class TestComm1060(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f200n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1060_%s.fits"
        cls.setup2()

class TestComm1061(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="None"
        cls.fname="C1061_%s.fits"
        cls.setup2()

class TestComm1062(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1062_%s.fits"
        cls.setup2()

class TestComm1063(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f212n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1063_%s.fits"
        cls.setup2()

class TestComm1064(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="None"
        cls.fname="C1064_%s.fits"
        cls.setup2()

class TestComm1065(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1065_%s.fits"
        cls.setup2()

class TestComm1066(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f215n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1066_%s.fits"
        cls.setup2()

class TestComm1067(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="None"
        cls.fname="C1067_%s.fits"
        cls.setup2()

class TestComm1068(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5000),band(bessell,h),20,vegamag)"
        cls.fname="C1068_%s.fits"
        cls.setup2()

class TestComm1069(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),20,vegamag)"
        cls.fname="C1069_%s.fits"
        cls.setup2()

class TestComm1070(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1070_%s.fits"
        cls.setup2()

class TestComm1071(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f222m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1071_%s.fits"
        cls.setup2()

class TestComm1072(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="None"
        cls.fname="C1072_%s.fits"
        cls.setup2()

class TestComm1073(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="rn(bb(5500),band(bessell,h),22,vegamag)"
        cls.fname="C1073_%s.fits"
        cls.setup2()

class TestComm1074(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,f240m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1074_%s.fits"
        cls.setup2()

class TestComm1075(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="None"
        cls.fname="C1075_%s.fits"
        cls.setup2()

class TestComm1076(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(bb(5000.0),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1076_%s.fits"
        cls.setup2()

class TestComm1077(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1077_%s.fits"
        cls.setup2()

class TestComm1078(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1078_%s.fits"
        cls.setup2()

class TestComm1079(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1079_%s.fits"
        cls.setup2()

class TestComm1080(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1080_%s.fits"
        cls.setup2()

class TestComm1081(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1081_%s.fits"
        cls.setup2()

class TestComm1082(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1082_%s.fits"
        cls.setup2()

class TestComm1083(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1083_%s.fits"
        cls.setup2()

class TestComm1084(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1084_%s.fits"
        cls.setup2()

class TestComm1085(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1085_%s.fits"
        cls.setup2()

class TestComm1086(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1086_%s.fits"
        cls.setup2()

class TestComm1087(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1087_%s.fits"
        cls.setup2()

class TestComm1088(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1088_%s.fits"
        cls.setup2()

class TestComm1089(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1089_%s.fits"
        cls.setup2()

class TestComm1090(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1090_%s.fits"
        cls.setup2()

class TestComm1091(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1091_%s.fits"
        cls.setup2()

class TestComm1092(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1092_%s.fits"
        cls.setup2()

class TestComm1093(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1093_%s.fits"
        cls.setup2()

class TestComm1094(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1094_%s.fits"
        cls.setup2()

class TestComm1095(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1095_%s.fits"
        cls.setup2()

class TestComm1096(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="rn(unit(1.0,flam),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1096_%s.fits"
        cls.setup2()

class TestComm1097(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1097_%s.fits"
        cls.setup2()

class TestComm1098(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1098_%s.fits"
        cls.setup2()

class TestComm1099(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1099_%s.fits"
        cls.setup2()

class TestComm1100(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1100_%s.fits"
        cls.setup2()

class TestComm1101(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1101_%s.fits"
        cls.setup2()

class TestComm1102(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g096"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1102_%s.fits"
        cls.setup2()

class TestComm1103(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="None"
        cls.fname="C1103_%s.fits"
        cls.setup2()

class TestComm1104(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1104_%s.fits"
        cls.setup2()

class TestComm1105(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1105_%s.fits"
        cls.setup2()

class TestComm1106(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1106_%s.fits"
        cls.setup2()

class TestComm1107(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1107_%s.fits"
        cls.setup2()

class TestComm1108(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1108_%s.fits"
        cls.setup2()

class TestComm1109(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1109_%s.fits"
        cls.setup2()

class TestComm1110(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1110_%s.fits"
        cls.setup2()

class TestComm1111(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1111_%s.fits"
        cls.setup2()

class TestComm1112(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1112_%s.fits"
        cls.setup2()

class TestComm1113(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1113_%s.fits"
        cls.setup2()

class TestComm1114(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1114_%s.fits"
        cls.setup2()

class TestComm1115(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-05,jy)"
        cls.fname="C1115_%s.fits"
        cls.setup2()

class TestComm1116(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.00E-06,jy)"
        cls.fname="C1116_%s.fits"
        cls.setup2()

class TestComm1117(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-12,flam)"
        cls.fname="C1117_%s.fits"
        cls.setup2()

class TestComm1118(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits)*ebmvx(1.0,gal1),box(10000.0,1.0),1.50E-13,flam)"
        cls.fname="C1118_%s.fits"
        cls.setup2()

class TestComm1119(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1119_%s.fits"
        cls.setup2()

class TestComm1120(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1120_%s.fits"
        cls.setup2()

class TestComm1121(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1121_%s.fits"
        cls.setup2()

class TestComm1122(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1122_%s.fits"
        cls.setup2()

class TestComm1123(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1123_%s.fits"
        cls.setup2()

class TestComm1124(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1124_%s.fits"
        cls.setup2()

class TestComm1125(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1125_%s.fits"
        cls.setup2()

class TestComm1126(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1126_%s.fits"
        cls.setup2()

class TestComm1127(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1127_%s.fits"
        cls.setup2()

class TestComm1128(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1128_%s.fits"
        cls.setup2()

class TestComm1129(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g141"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1129_%s.fits"
        cls.setup2()

class TestComm1130(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="None"
        cls.fname="C1130_%s.fits"
        cls.setup2()

class TestComm1131(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(ck04models,45000,0.0,4.5),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1131_%s.fits"
        cls.setup2()

class TestComm1132(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(1.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1132_%s.fits"
        cls.setup2()

class TestComm1133(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(5.0,gal1),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1133_%s.fits"
        cls.setup2()

class TestComm1134(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.554,vegamag)"
        cls.fname="C1134_%s.fits"
        cls.setup2()

class TestComm1135(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),12.658,vegamag)"
        cls.fname="C1135_%s.fits"
        cls.setup2()

class TestComm1136(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),15,vegamag)"
        cls.fname="C1136_%s.fits"
        cls.setup2()

class TestComm1137(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),band(nicmos,2,f110w),20,vegamag)"
        cls.fname="C1137_%s.fits"
        cls.setup2()

class TestComm1138(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.047,vegamag)"
        cls.fname="C1138_%s.fits"
        cls.setup2()

class TestComm1139(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),band(nicmos,2,f110w),14.185,vegamag)"
        cls.fname="C1139_%s.fits"
        cls.setup2()

class TestComm1140(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.735,vegamag)"
        cls.fname="C1140_%s.fits"
        cls.setup2()

class TestComm1141(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),band(nicmos,2,f110w),13.742,vegamag)"
        cls.fname="C1141_%s.fits"
        cls.setup2()

class TestComm1142(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1142_%s.fits"
        cls.setup2()

class TestComm1143(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1143_%s.fits"
        cls.setup2()

class TestComm1144(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),13,vegamag)"
        cls.fname="C1144_%s.fits"
        cls.setup2()

class TestComm1145(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(spec(egal.dat),band(nicmos,2,f110w),17,vegamag)"
        cls.fname="C1145_%s.fits"
        cls.setup2()

class TestComm1146(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1146_%s.fits"
        cls.setup2()

class TestComm1147(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1147_%s.fits"
        cls.setup2()

class TestComm1148(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1148_%s.fits"
        cls.setup2()

class TestComm1149(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.922913199593925,vegamag)"
        cls.fname="C1149_%s.fits"
        cls.setup2()

class TestComm1150(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)"
        cls.fname="C1150_%s.fits"
        cls.setup2()

class TestComm1151(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1151_%s.fits"
        cls.setup2()

class TestComm1152(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="nicmos,3,g206"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)"
        cls.fname="C1152_%s.fits"
        cls.setup2()

class TestComm1153(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd"
        cls.spectrum="rn(unit(1,flam),band(johnson,v),15.0,vegamag)"
        cls.fname="C1153_%s.fits"
        cls.setup2()

class TestComm1154(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10,vegamag)"
        cls.fname="C1154_%s.fits"
        cls.setup2()

class TestComm1155(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1155_%s.fits"
        cls.setup2()

class TestComm1156(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5),band(johnson,v),28,vegamag)"
        cls.fname="C1156_%s.fits"
        cls.setup2()

class TestComm1157(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        cls.fname="C1157_%s.fits"
        cls.setup2()

class TestComm1158(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1158_%s.fits"
        cls.setup2()

class TestComm1159(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1159_%s.fits"
        cls.setup2()

class TestComm1160(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1160_%s.fits"
        cls.setup2()

class TestComm1161(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,50ccd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1161_%s.fits"
        cls.setup2()

class TestComm1162(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f25nd5"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        cls.fname="C1162_%s.fits"
        cls.setup2()

class TestComm1163(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f25nd5"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1163_%s.fits"
        cls.setup2()

class TestComm1164(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1164_%s.fits"
        cls.setup2()

class TestComm1165(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1165_%s.fits"
        cls.setup2()

class TestComm1166(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1166_%s.fits"
        cls.setup2()

class TestComm1167(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1167_%s.fits"
        cls.setup2()

class TestComm1168(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oii"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1168_%s.fits"
        cls.setup2()

class TestComm1169(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1169_%s.fits"
        cls.setup2()

class TestComm1170(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oiii"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1170_%s.fits"
        cls.setup2()

class TestComm1171(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,f28x50oiii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1171_%s.fits"
        cls.setup2()

class TestComm1172(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1172_%s.fits"
        cls.setup2()

class TestComm1173(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1173_%s.fits"
        cls.setup2()

class TestComm1174(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        cls.fname="C1174_%s.fits"
        cls.setup2()

class TestComm1175(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230lb,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1175_%s.fits"
        cls.setup2()

class TestComm1176(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230mb,c1995"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1176_%s.fits"
        cls.setup2()

class TestComm1177(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g230mb,c1995,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1177_%s.fits"
        cls.setup2()

class TestComm1178(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        cls.fname="C1178_%s.fits"
        cls.setup2()

class TestComm1179(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1179_%s.fits"
        cls.setup2()

class TestComm1180(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1180_%s.fits"
        cls.setup2()

class TestComm1181(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1181_%s.fits"
        cls.setup2()

class TestComm1182(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1182_%s.fits"
        cls.setup2()

class TestComm1183(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23.5,vegamag)"
        cls.fname="C1183_%s.fits"
        cls.setup2()

class TestComm1184(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),10,vegamag)"
        cls.fname="C1184_%s.fits"
        cls.setup2()

class TestComm1185(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430l,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1185_%s.fits"
        cls.setup2()

class TestComm1186(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1186_%s.fits"
        cls.setup2()

class TestComm1187(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1187_%s.fits"
        cls.setup2()

class TestComm1188(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194,s52x2"
        cls.spectrum="em(4300.0,1.0,1.0E-12,flam)"
        cls.fname="C1188_%s.fits"
        cls.setup2()

class TestComm1189(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g430m,c4194,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1189_%s.fits"
        cls.setup2()

class TestComm1190(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1190_%s.fits"
        cls.setup2()

class TestComm1191(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1191_%s.fits"
        cls.setup2()

class TestComm1192(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1192_%s.fits"
        cls.setup2()

class TestComm1193(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1193_%s.fits"
        cls.setup2()

class TestComm1194(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1194_%s.fits"
        cls.setup2()

class TestComm1195(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1195_%s.fits"
        cls.setup2()

class TestComm1196(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),0.03),band(johnson,v),18,vegamag)"
        cls.fname="C1196_%s.fits"
        cls.setup2()

class TestComm1197(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),1.0),band(johnson,v),18,vegamag)"
        cls.fname="C1197_%s.fits"
        cls.setup2()

class TestComm1198(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x02"
        cls.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,v),18,vegamag)"
        cls.fname="C1198_%s.fits"
        cls.setup2()

class TestComm1199(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),23,vegamag)"
        cls.fname="C1199_%s.fits"
        cls.setup2()

class TestComm1200(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24.5,vegamag)"
        cls.fname="C1200_%s.fits"
        cls.setup2()

class TestComm1201(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750l,c7751,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1201_%s.fits"
        cls.setup2()

class TestComm1202(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750m,c7283"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1202_%s.fits"
        cls.setup2()

class TestComm1203(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,g750m,c7283,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1203_%s.fits"
        cls.setup2()

class TestComm1204(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),4,vegamag)"
        cls.fname="C1204_%s.fits"
        cls.setup2()

class TestComm1205(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"
        cls.fname="C1205_%s.fits"
        cls.setup2()

class TestComm1206(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1206_%s.fits"
        cls.setup2()

class TestComm1207(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,ccd,s03x005nd"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1207_%s.fits"
        cls.setup2()

class TestComm1208(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        cls.fname="C1208_%s.fits"
        cls.setup2()

class TestComm1209(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1209_%s.fits"
        cls.setup2()

class TestComm1210(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,25mama"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1210_%s.fits"
        cls.setup2()

class TestComm1211(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140h,c1416"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1211_%s.fits"
        cls.setup2()

class TestComm1212(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140h,c1416,s02x02"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1212_%s.fits"
        cls.setup2()

class TestComm1213(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1213_%s.fits"
        cls.setup2()

class TestComm1214(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1214_%s.fits"
        cls.setup2()

class TestComm1215(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1215_%s.fits"
        cls.setup2()

class TestComm1216(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        cls.spectrum="em(1425.0,0.043487548828125,1.0E-10,flam)"
        cls.fname="C1216_%s.fits"
        cls.setup2()

class TestComm1217(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x006"
        cls.spectrum="em(1425.0,1.0,1.0E-10,flam)"
        cls.fname="C1217_%s.fits"
        cls.setup2()

class TestComm1218(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),10,vegamag)"
        cls.fname="C1218_%s.fits"
        cls.setup2()

class TestComm1219(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),6,vegamag)"
        cls.fname="C1219_%s.fits"
        cls.setup2()

class TestComm1220(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0),band(johnson,v),7,vegamag)"
        cls.fname="C1220_%s.fits"
        cls.setup2()

class TestComm1221(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),22,vegamag)"
        cls.fname="C1221_%s.fits"
        cls.setup2()

class TestComm1222(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,e140m,c1425,s02x02"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1222_%s.fits"
        cls.setup2()

class TestComm1223(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25lya"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1223_%s.fits"
        cls.setup2()

class TestComm1224(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25lya"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1224_%s.fits"
        cls.setup2()

class TestComm1225(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25nd3"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1225_%s.fits"
        cls.setup2()

class TestComm1226(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25nd3"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1226_%s.fits"
        cls.setup2()

class TestComm1227(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq1"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1227_%s.fits"
        cls.setup2()

class TestComm1228(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq1"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1228_%s.fits"
        cls.setup2()

class TestComm1229(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq3"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1229_%s.fits"
        cls.setup2()

class TestComm1230(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25ndq3"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1230_%s.fits"
        cls.setup2()

class TestComm1231(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1231_%s.fits"
        cls.setup2()

class TestComm1232(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25qtz"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1232_%s.fits"
        cls.setup2()

class TestComm1233(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25srf2"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1233_%s.fits"
        cls.setup2()

class TestComm1234(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,f25srf2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1234_%s.fits"
        cls.setup2()

class TestComm1235(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1235_%s.fits"
        cls.setup2()

class TestComm1236(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1236_%s.fits"
        cls.setup2()

class TestComm1237(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x01"
        cls.spectrum="rn(spec(ngc1068_template.fits),band(johnson,v),9,vegamag)"
        cls.fname="C1237_%s.fits"
        cls.setup2()

class TestComm1238(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),13,vegamag)"
        cls.fname="C1238_%s.fits"
        cls.setup2()

class TestComm1239(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14,vegamag)"
        cls.fname="C1239_%s.fits"
        cls.setup2()

class TestComm1240(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),14.1,vegamag)"
        cls.fname="C1240_%s.fits"
        cls.setup2()

class TestComm1241(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),27.5,vegamag)"
        cls.fname="C1241_%s.fits"
        cls.setup2()

class TestComm1242(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),band(johnson,v),12.77,vegamag)"
        cls.fname="C1242_%s.fits"
        cls.setup2()

class TestComm1243(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),band(johnson,v),10.516,vegamag)"
        cls.fname="C1243_%s.fits"
        cls.setup2()

class TestComm1244(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140l,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        cls.fname="C1244_%s.fits"
        cls.setup2()

class TestComm1245(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140m,c1567"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1245_%s.fits"
        cls.setup2()

class TestComm1246(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,fuvmama,g140m,c1567,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1246_%s.fits"
        cls.setup2()

class TestComm1247(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C1247_%s.fits"
        cls.setup2()

class TestComm1248(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C1248_%s.fits"
        cls.setup2()

class TestComm1249(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C1249_%s.fits"
        cls.setup2()

class TestComm1250(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1215a.fits"
        cls.fname="C1250_%s.fits"
        cls.setup2()

class TestComm1251(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1302a.fits"
        cls.fname="C1251_%s.fits"
        cls.setup2()

class TestComm1252(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el1356a.fits"
        cls.fname="C1252_%s.fits"
        cls.setup2()

class TestComm1253(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g140l,fuvmama,s52x2"
        cls.spectrum="el2471a.fits"
        cls.fname="C1253_%s.fits"
        cls.setup2()

class TestComm1254(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C1254_%s.fits"
        cls.setup2()

class TestComm1255(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C1255_%s.fits"
        cls.setup2()

class TestComm1256(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230l,nuvmama,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C1256_%s.fits"
        cls.setup2()

class TestComm1257(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C1257_%s.fits"
        cls.setup2()

class TestComm1258(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C1258_%s.fits"
        cls.setup2()

class TestComm1259(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g230lb,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C1259_%s.fits"
        cls.setup2()

class TestComm1260(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C1260_%s.fits"
        cls.setup2()

class TestComm1261(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C1261_%s.fits"
        cls.setup2()

class TestComm1262(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g430l,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C1262_%s.fits"
        cls.setup2()

class TestComm1263(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/g191b2b_mod_004.fits"
        cls.fname="C1263_%s.fits"
        cls.setup2()

class TestComm1264(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd153_mod_004.fits"
        cls.fname="C1264_%s.fits"
        cls.setup2()

class TestComm1265(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,g750l,ccd,s52x2"
        cls.spectrum="/grp/hst/cdbs/calspec/gd71_mod_005.fits"
        cls.fname="C1265_%s.fits"
        cls.setup2()

class TestComm1266(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1266_%s.fits"
        cls.setup2()

class TestComm1267(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4),band(johnson,v),5,vegamag)"
        cls.fname="C1267_%s.fits"
        cls.setup2()

class TestComm1268(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,25mama"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1268_%s.fits"
        cls.setup2()

class TestComm1269(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1269_%s.fits"
        cls.setup2()

class TestComm1270(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(bb(50000),band(johnson,v),10.516,vegamag)"
        cls.fname="C1270_%s.fits"
        cls.setup2()

class TestComm1271(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),10.516,vegamag)"
        cls.fname="C1271_%s.fits"
        cls.setup2()

class TestComm1272(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(pl(4000.0,-1.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1272_%s.fits"
        cls.setup2()

class TestComm1273(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(pl(4000.0,0.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1273_%s.fits"
        cls.setup2()

class TestComm1274(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),band(johnson,v),10.516,vegamag)"
        cls.fname="C1274_%s.fits"
        cls.setup2()

class TestComm1275(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),box(2000.0,1.0),1.0e-12,flam)"
        cls.fname="C1275_%s.fits"
        cls.setup2()

class TestComm1276(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="rn(unit(1.0,flam),band(johnson,v),10.516,vegamag)"
        cls.fname="C1276_%s.fits"
        cls.setup2()

class TestComm1277(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230h,c2263,s02x02"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1277_%s.fits"
        cls.setup2()

class TestComm1278(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1278_%s.fits"
        cls.setup2()

class TestComm1279(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18.5,vegamag)"
        cls.fname="C1279_%s.fits"
        cls.setup2()

class TestComm1280(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,e230m,c1978,s02x02"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits)"
        cls.fname="C1280_%s.fits"
        cls.setup2()

class TestComm1281(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ciii"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1281_%s.fits"
        cls.setup2()

class TestComm1282(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ciii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1282_%s.fits"
        cls.setup2()

class TestComm1283(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn182"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1283_%s.fits"
        cls.setup2()

class TestComm1284(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn182"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1284_%s.fits"
        cls.setup2()

class TestComm1285(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn270"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1285_%s.fits"
        cls.setup2()

class TestComm1286(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25cn270"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1286_%s.fits"
        cls.setup2()

class TestComm1287(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25mgii"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1287_%s.fits"
        cls.setup2()

class TestComm1288(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25mgii"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1288_%s.fits"
        cls.setup2()

class TestComm1289(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25nd5"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1289_%s.fits"
        cls.setup2()

class TestComm1290(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25nd5"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1290_%s.fits"
        cls.setup2()

class TestComm1291(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1291_%s.fits"
        cls.setup2()

class TestComm1292(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1292_%s.fits"
        cls.setup2()

class TestComm1293(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq4"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1293_%s.fits"
        cls.setup2()

class TestComm1294(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25ndq4"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1294_%s.fits"
        cls.setup2()

class TestComm1295(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),18,vegamag)"
        cls.fname="C1295_%s.fits"
        cls.setup2()

class TestComm1296(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),20,vegamag)"
        cls.fname="C1296_%s.fits"
        cls.setup2()

class TestComm1297(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25qtz"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1297_%s.fits"
        cls.setup2()

class TestComm1298(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25srf2"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0),band(johnson,v),26,vegamag)"
        cls.fname="C1298_%s.fits"
        cls.setup2()

class TestComm1299(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,f25srf2"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1299_%s.fits"
        cls.setup2()

class TestComm1300(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1300_%s.fits"
        cls.setup2()

class TestComm1301(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1301_%s.fits"
        cls.setup2()

class TestComm1302(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,gal1),band(johnson,v),15,vegamag)"
        cls.fname="C1302_%s.fits"
        cls.setup2()

class TestComm1303(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,lmc),band(johnson,v),15,vegamag)"
        cls.fname="C1303_%s.fits"
        cls.setup2()

class TestComm1304(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,smc),band(johnson,v),15,vegamag)"
        cls.fname="C1304_%s.fits"
        cls.setup2()

class TestComm1305(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.5,xgal),band(johnson,v),15,vegamag)"
        cls.fname="C1305_%s.fits"
        cls.setup2()

class TestComm1306(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0),band(johnson,v),24,vegamag)"
        cls.fname="C1306_%s.fits"
        cls.setup2()

class TestComm1307(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230l,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits)"
        cls.fname="C1307_%s.fits"
        cls.setup2()

class TestComm1308(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230m,c2818"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1308_%s.fits"
        cls.setup2()

class TestComm1309(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,g230m,c2818,s52x2"
        cls.spectrum="spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits)"
        cls.fname="C1309_%s.fits"
        cls.setup2()

class TestComm1310(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1310_%s.fits"
        cls.setup2()

class TestComm1311(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism,s52x01"
        cls.spectrum="spec(HS20270651.dat)"
        cls.fname="C1311_%s.fits"
        cls.setup2()

class TestComm1312(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="stis,nuvmama,prism,s52x2"
        cls.spectrum="spec(HS20270651.dat)"
        cls.fname="C1312_%s.fits"
        cls.setup2()

class TestComm1313(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="None"
        cls.fname="C1313_%s.fits"
        cls.setup2()

class TestComm1314(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1314_%s.fits"
        cls.setup2()

class TestComm1315(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1315_%s.fits"
        cls.setup2()

class TestComm1316(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f098m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1316_%s.fits"
        cls.setup2()

class TestComm1317(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="None"
        cls.fname="C1317_%s.fits"
        cls.setup2()

class TestComm1318(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1318_%s.fits"
        cls.setup2()

class TestComm1319(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1319_%s.fits"
        cls.setup2()

class TestComm1320(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C1320_%s.fits"
        cls.setup2()

class TestComm1321(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C1321_%s.fits"
        cls.setup2()

class TestComm1322(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C1322_%s.fits"
        cls.setup2()

class TestComm1323(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1323_%s.fits"
        cls.setup2()

class TestComm1324(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1324_%s.fits"
        cls.setup2()

class TestComm1325(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1325_%s.fits"
        cls.setup2()

class TestComm1326(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f105w"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1326_%s.fits"
        cls.setup2()

class TestComm1327(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="None"
        cls.fname="C1327_%s.fits"
        cls.setup2()

class TestComm1328(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1328_%s.fits"
        cls.setup2()

class TestComm1329(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1329_%s.fits"
        cls.setup2()

class TestComm1330(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1330_%s.fits"
        cls.setup2()

class TestComm1331(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1331_%s.fits"
        cls.setup2()

class TestComm1332(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1332_%s.fits"
        cls.setup2()

class TestComm1333(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1333_%s.fits"
        cls.setup2()

class TestComm1334(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1334_%s.fits"
        cls.setup2()

class TestComm1335(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1335_%s.fits"
        cls.setup2()

class TestComm1336(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1336_%s.fits"
        cls.setup2()

class TestComm1337(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1337_%s.fits"
        cls.setup2()

class TestComm1338(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1338_%s.fits"
        cls.setup2()

class TestComm1339(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1339_%s.fits"
        cls.setup2()

class TestComm1340(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1340_%s.fits"
        cls.setup2()

class TestComm1341(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1341_%s.fits"
        cls.setup2()

class TestComm1342(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1342_%s.fits"
        cls.setup2()

class TestComm1343(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1343_%s.fits"
        cls.setup2()

class TestComm1344(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1344_%s.fits"
        cls.setup2()

class TestComm1345(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1345_%s.fits"
        cls.setup2()

class TestComm1346(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1346_%s.fits"
        cls.setup2()

class TestComm1347(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1347_%s.fits"
        cls.setup2()

class TestComm1348(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1348_%s.fits"
        cls.setup2()

class TestComm1349(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1349_%s.fits"
        cls.setup2()

class TestComm1350(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1350_%s.fits"
        cls.setup2()

class TestComm1351(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1351_%s.fits"
        cls.setup2()

class TestComm1352(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1352_%s.fits"
        cls.setup2()

class TestComm1353(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1353_%s.fits"
        cls.setup2()

class TestComm1354(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f110w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1354_%s.fits"
        cls.setup2()

class TestComm1355(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="None"
        cls.fname="C1355_%s.fits"
        cls.setup2()

class TestComm1356(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1356_%s.fits"
        cls.setup2()

class TestComm1357(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1357_%s.fits"
        cls.setup2()

class TestComm1358(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1358_%s.fits"
        cls.setup2()

class TestComm1359(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1359_%s.fits"
        cls.setup2()

class TestComm1360(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1360_%s.fits"
        cls.setup2()

class TestComm1361(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1361_%s.fits"
        cls.setup2()

class TestComm1362(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1362_%s.fits"
        cls.setup2()

class TestComm1363(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1363_%s.fits"
        cls.setup2()

class TestComm1364(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1364_%s.fits"
        cls.setup2()

class TestComm1365(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1365_%s.fits"
        cls.setup2()

class TestComm1366(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1366_%s.fits"
        cls.setup2()

class TestComm1367(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1367_%s.fits"
        cls.setup2()

class TestComm1368(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1368_%s.fits"
        cls.setup2()

class TestComm1369(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f125w"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1369_%s.fits"
        cls.setup2()

class TestComm1370(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="None"
        cls.fname="C1370_%s.fits"
        cls.setup2()

class TestComm1371(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1371_%s.fits"
        cls.setup2()

class TestComm1372(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1372_%s.fits"
        cls.setup2()

class TestComm1373(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f126n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1373_%s.fits"
        cls.setup2()

class TestComm1374(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="None"
        cls.fname="C1374_%s.fits"
        cls.setup2()

class TestComm1375(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1375_%s.fits"
        cls.setup2()

class TestComm1376(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1376_%s.fits"
        cls.setup2()

class TestComm1377(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f127m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1377_%s.fits"
        cls.setup2()

class TestComm1378(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="None"
        cls.fname="C1378_%s.fits"
        cls.setup2()

class TestComm1379(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1379_%s.fits"
        cls.setup2()

class TestComm1380(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1380_%s.fits"
        cls.setup2()

class TestComm1381(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f128n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1381_%s.fits"
        cls.setup2()

class TestComm1382(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="None"
        cls.fname="C1382_%s.fits"
        cls.setup2()

class TestComm1383(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1383_%s.fits"
        cls.setup2()

class TestComm1384(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1384_%s.fits"
        cls.setup2()

class TestComm1385(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f130n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1385_%s.fits"
        cls.setup2()

class TestComm1386(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="None"
        cls.fname="C1386_%s.fits"
        cls.setup2()

class TestComm1387(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1387_%s.fits"
        cls.setup2()

class TestComm1388(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1388_%s.fits"
        cls.setup2()

class TestComm1389(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(13200.0,5.0,1.0E-13,flam)"
        cls.fname="C1389_%s.fits"
        cls.setup2()

class TestComm1390(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f132n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1390_%s.fits"
        cls.setup2()

class TestComm1391(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="None"
        cls.fname="C1391_%s.fits"
        cls.setup2()

class TestComm1392(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1392_%s.fits"
        cls.setup2()

class TestComm1393(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1393_%s.fits"
        cls.setup2()

class TestComm1394(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f139m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1394_%s.fits"
        cls.setup2()

class TestComm1395(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="None"
        cls.fname="C1395_%s.fits"
        cls.setup2()

class TestComm1396(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1396_%s.fits"
        cls.setup2()

class TestComm1397(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1397_%s.fits"
        cls.setup2()

class TestComm1398(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1398_%s.fits"
        cls.setup2()

class TestComm1399(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1399_%s.fits"
        cls.setup2()

class TestComm1400(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1400_%s.fits"
        cls.setup2()

class TestComm1401(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(egal.dat),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1401_%s.fits"
        cls.setup2()

class TestComm1402(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(egal.dat),1.0),band(johnson,b),28.0,vegamag)"
        cls.fname="C1402_%s.fits"
        cls.setup2()

class TestComm1403(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(qso_template.fits),3.0),band(johnson,b),28.0,vegamag)"
        cls.fname="C1403_%s.fits"
        cls.setup2()

class TestComm1404(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(spiral.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1404_%s.fits"
        cls.setup2()

class TestComm1405(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="rn(z(spec(spiral.fits),2.0),band(johnson,b),28.0,vegamag)"
        cls.fname="C1405_%s.fits"
        cls.setup2()

class TestComm1406(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f140w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1406_%s.fits"
        cls.setup2()

class TestComm1407(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="None"
        cls.fname="C1407_%s.fits"
        cls.setup2()

class TestComm1408(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1408_%s.fits"
        cls.setup2()

class TestComm1409(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1409_%s.fits"
        cls.setup2()

class TestComm1410(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        cls.fname="C1410_%s.fits"
        cls.setup2()

class TestComm1411(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        cls.fname="C1411_%s.fits"
        cls.setup2()

class TestComm1412(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        cls.fname="C1412_%s.fits"
        cls.setup2()

class TestComm1413(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        cls.fname="C1413_%s.fits"
        cls.setup2()

class TestComm1414(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1414_%s.fits"
        cls.setup2()

class TestComm1415(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1415_%s.fits"
        cls.setup2()

class TestComm1416(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1416_%s.fits"
        cls.setup2()

class TestComm1417(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f153m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1417_%s.fits"
        cls.setup2()

class TestComm1418(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="None"
        cls.fname="C1418_%s.fits"
        cls.setup2()

class TestComm1419(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1419_%s.fits"
        cls.setup2()

class TestComm1420(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1420_%s.fits"
        cls.setup2()

class TestComm1421(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1421_%s.fits"
        cls.setup2()

class TestComm1422(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1422_%s.fits"
        cls.setup2()

class TestComm1423(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1423_%s.fits"
        cls.setup2()

class TestComm1424(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1424_%s.fits"
        cls.setup2()

class TestComm1425(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1425_%s.fits"
        cls.setup2()

class TestComm1426(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1426_%s.fits"
        cls.setup2()

class TestComm1427(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1427_%s.fits"
        cls.setup2()

class TestComm1428(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1428_%s.fits"
        cls.setup2()

class TestComm1429(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1429_%s.fits"
        cls.setup2()

class TestComm1430(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1430_%s.fits"
        cls.setup2()

class TestComm1431(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1431_%s.fits"
        cls.setup2()

class TestComm1432(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1432_%s.fits"
        cls.setup2()

class TestComm1433(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1433_%s.fits"
        cls.setup2()

class TestComm1434(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1434_%s.fits"
        cls.setup2()

class TestComm1435(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1435_%s.fits"
        cls.setup2()

class TestComm1436(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1436_%s.fits"
        cls.setup2()

class TestComm1437(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1437_%s.fits"
        cls.setup2()

class TestComm1438(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1438_%s.fits"
        cls.setup2()

class TestComm1439(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1439_%s.fits"
        cls.setup2()

class TestComm1440(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1440_%s.fits"
        cls.setup2()

class TestComm1441(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1441_%s.fits"
        cls.setup2()

class TestComm1442(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1442_%s.fits"
        cls.setup2()

class TestComm1443(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1443_%s.fits"
        cls.setup2()

class TestComm1444(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1444_%s.fits"
        cls.setup2()

class TestComm1445(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1445_%s.fits"
        cls.setup2()

class TestComm1446(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1446_%s.fits"
        cls.setup2()

class TestComm1447(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1447_%s.fits"
        cls.setup2()

class TestComm1448(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1448_%s.fits"
        cls.setup2()

class TestComm1449(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1449_%s.fits"
        cls.setup2()

class TestComm1450(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1450_%s.fits"
        cls.setup2()

class TestComm1451(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1451_%s.fits"
        cls.setup2()

class TestComm1452(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1452_%s.fits"
        cls.setup2()

class TestComm1453(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1453_%s.fits"
        cls.setup2()

class TestComm1454(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1454_%s.fits"
        cls.setup2()

class TestComm1455(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1455_%s.fits"
        cls.setup2()

class TestComm1456(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1456_%s.fits"
        cls.setup2()

class TestComm1457(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1457_%s.fits"
        cls.setup2()

class TestComm1458(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1458_%s.fits"
        cls.setup2()

class TestComm1459(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1459_%s.fits"
        cls.setup2()

class TestComm1460(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1460_%s.fits"
        cls.setup2()

class TestComm1461(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1461_%s.fits"
        cls.setup2()

class TestComm1462(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1462_%s.fits"
        cls.setup2()

class TestComm1463(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1463_%s.fits"
        cls.setup2()

class TestComm1464(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1464_%s.fits"
        cls.setup2()

class TestComm1465(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1465_%s.fits"
        cls.setup2()

class TestComm1466(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1466_%s.fits"
        cls.setup2()

class TestComm1467(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1467_%s.fits"
        cls.setup2()

class TestComm1468(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1468_%s.fits"
        cls.setup2()

class TestComm1469(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1469_%s.fits"
        cls.setup2()

class TestComm1470(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1470_%s.fits"
        cls.setup2()

class TestComm1471(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1471_%s.fits"
        cls.setup2()

class TestComm1472(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1472_%s.fits"
        cls.setup2()

class TestComm1473(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1473_%s.fits"
        cls.setup2()

class TestComm1474(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1474_%s.fits"
        cls.setup2()

class TestComm1475(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1475_%s.fits"
        cls.setup2()

class TestComm1476(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1476_%s.fits"
        cls.setup2()

class TestComm1477(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1477_%s.fits"
        cls.setup2()

class TestComm1478(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1478_%s.fits"
        cls.setup2()

class TestComm1479(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1479_%s.fits"
        cls.setup2()

class TestComm1480(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1480_%s.fits"
        cls.setup2()

class TestComm1481(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1481_%s.fits"
        cls.setup2()

class TestComm1482(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1482_%s.fits"
        cls.setup2()

class TestComm1483(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1483_%s.fits"
        cls.setup2()

class TestComm1484(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1484_%s.fits"
        cls.setup2()

class TestComm1485(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1485_%s.fits"
        cls.setup2()

class TestComm1486(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1486_%s.fits"
        cls.setup2()

class TestComm1487(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1487_%s.fits"
        cls.setup2()

class TestComm1488(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1488_%s.fits"
        cls.setup2()

class TestComm1489(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1489_%s.fits"
        cls.setup2()

class TestComm1490(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1490_%s.fits"
        cls.setup2()

class TestComm1491(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1491_%s.fits"
        cls.setup2()

class TestComm1492(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1492_%s.fits"
        cls.setup2()

class TestComm1493(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f160w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1493_%s.fits"
        cls.setup2()

class TestComm1494(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="None"
        cls.fname="C1494_%s.fits"
        cls.setup2()

class TestComm1495(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1495_%s.fits"
        cls.setup2()

class TestComm1496(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1496_%s.fits"
        cls.setup2()

class TestComm1497(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f164n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1497_%s.fits"
        cls.setup2()

class TestComm1498(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="None"
        cls.fname="C1498_%s.fits"
        cls.setup2()

class TestComm1499(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1499_%s.fits"
        cls.setup2()

class TestComm1500(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1500_%s.fits"
        cls.setup2()

class TestComm1501(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,f167n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1501_%s.fits"
        cls.setup2()

class TestComm1502(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1502_%s.fits"
        cls.setup2()

class TestComm1503(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1503_%s.fits"
        cls.setup2()

class TestComm1504(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C1504_%s.fits"
        cls.setup2()

class TestComm1505(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1505_%s.fits"
        cls.setup2()

class TestComm1506(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1506_%s.fits"
        cls.setup2()

class TestComm1507(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C1507_%s.fits"
        cls.setup2()

class TestComm1508(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1508_%s.fits"
        cls.setup2()

class TestComm1509(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1509_%s.fits"
        cls.setup2()

class TestComm1510(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1510_%s.fits"
        cls.setup2()

class TestComm1511(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C1511_%s.fits"
        cls.setup2()

class TestComm1512(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C1512_%s.fits"
        cls.setup2()

class TestComm1513(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C1513_%s.fits"
        cls.setup2()

class TestComm1514(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C1514_%s.fits"
        cls.setup2()

class TestComm1515(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1515_%s.fits"
        cls.setup2()

class TestComm1516(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C1516_%s.fits"
        cls.setup2()

class TestComm1517(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="None"
        cls.fname="C1517_%s.fits"
        cls.setup2()

class TestComm1518(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1518_%s.fits"
        cls.setup2()

class TestComm1519(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1519_%s.fits"
        cls.setup2()

class TestComm1520(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1520_%s.fits"
        cls.setup2()

class TestComm1521(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g102,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1521_%s.fits"
        cls.setup2()

class TestComm1522(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C1522_%s.fits"
        cls.setup2()

class TestComm1523(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C1523_%s.fits"
        cls.setup2()

class TestComm1524(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C1524_%s.fits"
        cls.setup2()

class TestComm1525(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C1525_%s.fits"
        cls.setup2()

class TestComm1526(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C1526_%s.fits"
        cls.setup2()

class TestComm1527(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C1527_%s.fits"
        cls.setup2()

class TestComm1528(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1528_%s.fits"
        cls.setup2()

class TestComm1529(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1529_%s.fits"
        cls.setup2()

class TestComm1530(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1530_%s.fits"
        cls.setup2()

class TestComm1531(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1531_%s.fits"
        cls.setup2()

class TestComm1532(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1532_%s.fits"
        cls.setup2()

class TestComm1533(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1533_%s.fits"
        cls.setup2()

class TestComm1534(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1534_%s.fits"
        cls.setup2()

class TestComm1535(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1535_%s.fits"
        cls.setup2()

class TestComm1536(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1536_%s.fits"
        cls.setup2()

class TestComm1537(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1537_%s.fits"
        cls.setup2()

class TestComm1538(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1538_%s.fits"
        cls.setup2()

class TestComm1539(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1539_%s.fits"
        cls.setup2()

class TestComm1540(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1540_%s.fits"
        cls.setup2()

class TestComm1541(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1541_%s.fits"
        cls.setup2()

class TestComm1542(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1542_%s.fits"
        cls.setup2()

class TestComm1543(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1543_%s.fits"
        cls.setup2()

class TestComm1544(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1544_%s.fits"
        cls.setup2()

class TestComm1545(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="None"
        cls.fname="C1545_%s.fits"
        cls.setup2()

class TestComm1546(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1546_%s.fits"
        cls.setup2()

class TestComm1547(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1547_%s.fits"
        cls.setup2()

class TestComm1548(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1548_%s.fits"
        cls.setup2()

class TestComm1549(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1549_%s.fits"
        cls.setup2()

class TestComm1550(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1550_%s.fits"
        cls.setup2()

class TestComm1551(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,ir,g141,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1551_%s.fits"
        cls.setup2()

class TestComm1552(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1552_%s.fits"
        cls.setup2()

class TestComm1553(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1553_%s.fits"
        cls.setup2()

class TestComm1554(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f200lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1554_%s.fits"
        cls.setup2()

class TestComm1555(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1555_%s.fits"
        cls.setup2()

class TestComm1556(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1556_%s.fits"
        cls.setup2()

class TestComm1557(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f218w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1557_%s.fits"
        cls.setup2()

class TestComm1558(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1558_%s.fits"
        cls.setup2()

class TestComm1559(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1559_%s.fits"
        cls.setup2()

class TestComm1560(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        cls.fname="C1560_%s.fits"
        cls.setup2()

class TestComm1561(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        cls.fname="C1561_%s.fits"
        cls.setup2()

class TestComm1562(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        cls.fname="C1562_%s.fits"
        cls.setup2()

class TestComm1563(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        cls.fname="C1563_%s.fits"
        cls.setup2()

class TestComm1564(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1564_%s.fits"
        cls.setup2()

class TestComm1565(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1565_%s.fits"
        cls.setup2()

class TestComm1566(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1566_%s.fits"
        cls.setup2()

class TestComm1567(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1567_%s.fits"
        cls.setup2()

class TestComm1568(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1568_%s.fits"
        cls.setup2()

class TestComm1569(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1569_%s.fits"
        cls.setup2()

class TestComm1570(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f275w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1570_%s.fits"
        cls.setup2()

class TestComm1571(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1571_%s.fits"
        cls.setup2()

class TestComm1572(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1572_%s.fits"
        cls.setup2()

class TestComm1573(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f280n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1573_%s.fits"
        cls.setup2()

class TestComm1574(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1574_%s.fits"
        cls.setup2()

class TestComm1575(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1575_%s.fits"
        cls.setup2()

class TestComm1576(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1576_%s.fits"
        cls.setup2()

class TestComm1577(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1577_%s.fits"
        cls.setup2()

class TestComm1578(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1578_%s.fits"
        cls.setup2()

class TestComm1579(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1579_%s.fits"
        cls.setup2()

class TestComm1580(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1580_%s.fits"
        cls.setup2()

class TestComm1581(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1581_%s.fits"
        cls.setup2()

class TestComm1582(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1582_%s.fits"
        cls.setup2()

class TestComm1583(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1583_%s.fits"
        cls.setup2()

class TestComm1584(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1584_%s.fits"
        cls.setup2()

class TestComm1585(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1585_%s.fits"
        cls.setup2()

class TestComm1586(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1586_%s.fits"
        cls.setup2()

class TestComm1587(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1587_%s.fits"
        cls.setup2()

class TestComm1588(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1588_%s.fits"
        cls.setup2()

class TestComm1589(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1589_%s.fits"
        cls.setup2()

class TestComm1590(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f336w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1590_%s.fits"
        cls.setup2()

class TestComm1591(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1591_%s.fits"
        cls.setup2()

class TestComm1592(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1592_%s.fits"
        cls.setup2()

class TestComm1593(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f343n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1593_%s.fits"
        cls.setup2()

class TestComm1594(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1594_%s.fits"
        cls.setup2()

class TestComm1595(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1595_%s.fits"
        cls.setup2()

class TestComm1596(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f350lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1596_%s.fits"
        cls.setup2()

class TestComm1597(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1597_%s.fits"
        cls.setup2()

class TestComm1598(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1598_%s.fits"
        cls.setup2()

class TestComm1599(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f373n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1599_%s.fits"
        cls.setup2()

class TestComm1600(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1600_%s.fits"
        cls.setup2()

class TestComm1601(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1601_%s.fits"
        cls.setup2()

class TestComm1602(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1602_%s.fits"
        cls.setup2()

class TestComm1603(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1603_%s.fits"
        cls.setup2()

class TestComm1604(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1604_%s.fits"
        cls.setup2()

class TestComm1605(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f390w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1605_%s.fits"
        cls.setup2()

class TestComm1606(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1606_%s.fits"
        cls.setup2()

class TestComm1607(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1607_%s.fits"
        cls.setup2()

class TestComm1608(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f395n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1608_%s.fits"
        cls.setup2()

class TestComm1609(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1609_%s.fits"
        cls.setup2()

class TestComm1610(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1610_%s.fits"
        cls.setup2()

class TestComm1611(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f410m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1611_%s.fits"
        cls.setup2()

class TestComm1612(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1612_%s.fits"
        cls.setup2()

class TestComm1613(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1613_%s.fits"
        cls.setup2()

class TestComm1614(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f438w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1614_%s.fits"
        cls.setup2()

class TestComm1615(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1615_%s.fits"
        cls.setup2()

class TestComm1616(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1616_%s.fits"
        cls.setup2()

class TestComm1617(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f467m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1617_%s.fits"
        cls.setup2()

class TestComm1618(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1618_%s.fits"
        cls.setup2()

class TestComm1619(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1619_%s.fits"
        cls.setup2()

class TestComm1620(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f469n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1620_%s.fits"
        cls.setup2()

class TestComm1621(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1621_%s.fits"
        cls.setup2()

class TestComm1622(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1622_%s.fits"
        cls.setup2()

class TestComm1623(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1623_%s.fits"
        cls.setup2()

class TestComm1624(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1624_%s.fits"
        cls.setup2()

class TestComm1625(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1625_%s.fits"
        cls.setup2()

class TestComm1626(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f475x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1626_%s.fits"
        cls.setup2()

class TestComm1627(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1627_%s.fits"
        cls.setup2()

class TestComm1628(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1628_%s.fits"
        cls.setup2()

class TestComm1629(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f487n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1629_%s.fits"
        cls.setup2()

class TestComm1630(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1630_%s.fits"
        cls.setup2()

class TestComm1631(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1631_%s.fits"
        cls.setup2()

class TestComm1632(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        cls.fname="C1632_%s.fits"
        cls.setup2()

class TestComm1633(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1633_%s.fits"
        cls.setup2()

class TestComm1634(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1634_%s.fits"
        cls.setup2()

class TestComm1635(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1635_%s.fits"
        cls.setup2()

class TestComm1636(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f547m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1636_%s.fits"
        cls.setup2()

class TestComm1637(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1637_%s.fits"
        cls.setup2()

class TestComm1638(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1638_%s.fits"
        cls.setup2()

class TestComm1639(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1639_%s.fits"
        cls.setup2()

class TestComm1640(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1640_%s.fits"
        cls.setup2()

class TestComm1641(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1641_%s.fits"
        cls.setup2()

class TestComm1642(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1642_%s.fits"
        cls.setup2()

class TestComm1643(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1643_%s.fits"
        cls.setup2()

class TestComm1644(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1644_%s.fits"
        cls.setup2()

class TestComm1645(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1645_%s.fits"
        cls.setup2()

class TestComm1646(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1646_%s.fits"
        cls.setup2()

class TestComm1647(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1647_%s.fits"
        cls.setup2()

class TestComm1648(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1648_%s.fits"
        cls.setup2()

class TestComm1649(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1649_%s.fits"
        cls.setup2()

class TestComm1650(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1650_%s.fits"
        cls.setup2()

class TestComm1651(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1651_%s.fits"
        cls.setup2()

class TestComm1652(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1652_%s.fits"
        cls.setup2()

class TestComm1653(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1653_%s.fits"
        cls.setup2()

class TestComm1654(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1654_%s.fits"
        cls.setup2()

class TestComm1655(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1655_%s.fits"
        cls.setup2()

class TestComm1656(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1656_%s.fits"
        cls.setup2()

class TestComm1657(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1657_%s.fits"
        cls.setup2()

class TestComm1658(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1658_%s.fits"
        cls.setup2()

class TestComm1659(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1659_%s.fits"
        cls.setup2()

class TestComm1660(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1660_%s.fits"
        cls.setup2()

class TestComm1661(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C1661_%s.fits"
        cls.setup2()

class TestComm1662(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C1662_%s.fits"
        cls.setup2()

class TestComm1663(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C1663_%s.fits"
        cls.setup2()

class TestComm1664(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1664_%s.fits"
        cls.setup2()

class TestComm1665(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C1665_%s.fits"
        cls.setup2()

class TestComm1666(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1666_%s.fits"
        cls.setup2()

class TestComm1667(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1667_%s.fits"
        cls.setup2()

class TestComm1668(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1668_%s.fits"
        cls.setup2()

class TestComm1669(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1669_%s.fits"
        cls.setup2()

class TestComm1670(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f600lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1670_%s.fits"
        cls.setup2()

class TestComm1671(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1671_%s.fits"
        cls.setup2()

class TestComm1672(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1672_%s.fits"
        cls.setup2()

class TestComm1673(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1673_%s.fits"
        cls.setup2()

class TestComm1674(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1674_%s.fits"
        cls.setup2()

class TestComm1675(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1675_%s.fits"
        cls.setup2()

class TestComm1676(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1676_%s.fits"
        cls.setup2()

class TestComm1677(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1677_%s.fits"
        cls.setup2()

class TestComm1678(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1678_%s.fits"
        cls.setup2()

class TestComm1679(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1679_%s.fits"
        cls.setup2()

class TestComm1680(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1680_%s.fits"
        cls.setup2()

class TestComm1681(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1681_%s.fits"
        cls.setup2()

class TestComm1682(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1682_%s.fits"
        cls.setup2()

class TestComm1683(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1683_%s.fits"
        cls.setup2()

class TestComm1684(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1684_%s.fits"
        cls.setup2()

class TestComm1685(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1685_%s.fits"
        cls.setup2()

class TestComm1686(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1686_%s.fits"
        cls.setup2()

class TestComm1687(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1687_%s.fits"
        cls.setup2()

class TestComm1688(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1688_%s.fits"
        cls.setup2()

class TestComm1689(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1689_%s.fits"
        cls.setup2()

class TestComm1690(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C1690_%s.fits"
        cls.setup2()

class TestComm1691(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C1691_%s.fits"
        cls.setup2()

class TestComm1692(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1692_%s.fits"
        cls.setup2()

class TestComm1693(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C1693_%s.fits"
        cls.setup2()

class TestComm1694(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C1694_%s.fits"
        cls.setup2()

class TestComm1695(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1695_%s.fits"
        cls.setup2()

class TestComm1696(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1696_%s.fits"
        cls.setup2()

class TestComm1697(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1697_%s.fits"
        cls.setup2()

class TestComm1698(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1698_%s.fits"
        cls.setup2()

class TestComm1699(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1699_%s.fits"
        cls.setup2()

class TestComm1700(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f621m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1700_%s.fits"
        cls.setup2()

class TestComm1701(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1701_%s.fits"
        cls.setup2()

class TestComm1702(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1702_%s.fits"
        cls.setup2()

class TestComm1703(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1703_%s.fits"
        cls.setup2()

class TestComm1704(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1704_%s.fits"
        cls.setup2()

class TestComm1705(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1705_%s.fits"
        cls.setup2()

class TestComm1706(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f631n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1706_%s.fits"
        cls.setup2()

class TestComm1707(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1707_%s.fits"
        cls.setup2()

class TestComm1708(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1708_%s.fits"
        cls.setup2()

class TestComm1709(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f645n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1709_%s.fits"
        cls.setup2()

class TestComm1710(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1710_%s.fits"
        cls.setup2()

class TestComm1711(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1711_%s.fits"
        cls.setup2()

class TestComm1712(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f656n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1712_%s.fits"
        cls.setup2()

class TestComm1713(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1713_%s.fits"
        cls.setup2()

class TestComm1714(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1714_%s.fits"
        cls.setup2()

class TestComm1715(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f657n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1715_%s.fits"
        cls.setup2()

class TestComm1716(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1716_%s.fits"
        cls.setup2()

class TestComm1717(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1717_%s.fits"
        cls.setup2()

class TestComm1718(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1718_%s.fits"
        cls.setup2()

class TestComm1719(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1719_%s.fits"
        cls.setup2()

class TestComm1720(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1720_%s.fits"
        cls.setup2()

class TestComm1721(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f665n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1721_%s.fits"
        cls.setup2()

class TestComm1722(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1722_%s.fits"
        cls.setup2()

class TestComm1723(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1723_%s.fits"
        cls.setup2()

class TestComm1724(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f673n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1724_%s.fits"
        cls.setup2()

class TestComm1725(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1725_%s.fits"
        cls.setup2()

class TestComm1726(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1726_%s.fits"
        cls.setup2()

class TestComm1727(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f680n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1727_%s.fits"
        cls.setup2()

class TestComm1728(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1728_%s.fits"
        cls.setup2()

class TestComm1729(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1729_%s.fits"
        cls.setup2()

class TestComm1730(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f689m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1730_%s.fits"
        cls.setup2()

class TestComm1731(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1731_%s.fits"
        cls.setup2()

class TestComm1732(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1732_%s.fits"
        cls.setup2()

class TestComm1733(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f763m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1733_%s.fits"
        cls.setup2()

class TestComm1734(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1734_%s.fits"
        cls.setup2()

class TestComm1735(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1735_%s.fits"
        cls.setup2()

class TestComm1736(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1736_%s.fits"
        cls.setup2()

class TestComm1737(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1737_%s.fits"
        cls.setup2()

class TestComm1738(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1738_%s.fits"
        cls.setup2()

class TestComm1739(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1739_%s.fits"
        cls.setup2()

class TestComm1740(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1740_%s.fits"
        cls.setup2()

class TestComm1741(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1741_%s.fits"
        cls.setup2()

class TestComm1742(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1742_%s.fits"
        cls.setup2()

class TestComm1743(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1743_%s.fits"
        cls.setup2()

class TestComm1744(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1744_%s.fits"
        cls.setup2()

class TestComm1745(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1745_%s.fits"
        cls.setup2()

class TestComm1746(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1746_%s.fits"
        cls.setup2()

class TestComm1747(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1747_%s.fits"
        cls.setup2()

class TestComm1748(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1748_%s.fits"
        cls.setup2()

class TestComm1749(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1749_%s.fits"
        cls.setup2()

class TestComm1750(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1750_%s.fits"
        cls.setup2()

class TestComm1751(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1751_%s.fits"
        cls.setup2()

class TestComm1752(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1752_%s.fits"
        cls.setup2()

class TestComm1753(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1753_%s.fits"
        cls.setup2()

class TestComm1754(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1754_%s.fits"
        cls.setup2()

class TestComm1755(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1755_%s.fits"
        cls.setup2()

class TestComm1756(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1756_%s.fits"
        cls.setup2()

class TestComm1757(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1757_%s.fits"
        cls.setup2()

class TestComm1758(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1758_%s.fits"
        cls.setup2()

class TestComm1759(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1759_%s.fits"
        cls.setup2()

class TestComm1760(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1760_%s.fits"
        cls.setup2()

class TestComm1761(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1761_%s.fits"
        cls.setup2()

class TestComm1762(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1762_%s.fits"
        cls.setup2()

class TestComm1763(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1763_%s.fits"
        cls.setup2()

class TestComm1764(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1764_%s.fits"
        cls.setup2()

class TestComm1765(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1765_%s.fits"
        cls.setup2()

class TestComm1766(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1766_%s.fits"
        cls.setup2()

class TestComm1767(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1767_%s.fits"
        cls.setup2()

class TestComm1768(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1768_%s.fits"
        cls.setup2()

class TestComm1769(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1769_%s.fits"
        cls.setup2()

class TestComm1770(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1770_%s.fits"
        cls.setup2()

class TestComm1771(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1771_%s.fits"
        cls.setup2()

class TestComm1772(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1772_%s.fits"
        cls.setup2()

class TestComm1773(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1773_%s.fits"
        cls.setup2()

class TestComm1774(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1774_%s.fits"
        cls.setup2()

class TestComm1775(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1775_%s.fits"
        cls.setup2()

class TestComm1776(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1776_%s.fits"
        cls.setup2()

class TestComm1777(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1777_%s.fits"
        cls.setup2()

class TestComm1778(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1778_%s.fits"
        cls.setup2()

class TestComm1779(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1779_%s.fits"
        cls.setup2()

class TestComm1780(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1780_%s.fits"
        cls.setup2()

class TestComm1781(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1781_%s.fits"
        cls.setup2()

class TestComm1782(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1782_%s.fits"
        cls.setup2()

class TestComm1783(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1783_%s.fits"
        cls.setup2()

class TestComm1784(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1784_%s.fits"
        cls.setup2()

class TestComm1785(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1785_%s.fits"
        cls.setup2()

class TestComm1786(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1786_%s.fits"
        cls.setup2()

class TestComm1787(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1787_%s.fits"
        cls.setup2()

class TestComm1788(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1788_%s.fits"
        cls.setup2()

class TestComm1789(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1789_%s.fits"
        cls.setup2()

class TestComm1790(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1790_%s.fits"
        cls.setup2()

class TestComm1791(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1791_%s.fits"
        cls.setup2()

class TestComm1792(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1792_%s.fits"
        cls.setup2()

class TestComm1793(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1793_%s.fits"
        cls.setup2()

class TestComm1794(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1794_%s.fits"
        cls.setup2()

class TestComm1795(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1795_%s.fits"
        cls.setup2()

class TestComm1796(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1796_%s.fits"
        cls.setup2()

class TestComm1797(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1797_%s.fits"
        cls.setup2()

class TestComm1798(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1798_%s.fits"
        cls.setup2()

class TestComm1799(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1799_%s.fits"
        cls.setup2()

class TestComm1800(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1800_%s.fits"
        cls.setup2()

class TestComm1801(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1801_%s.fits"
        cls.setup2()

class TestComm1802(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1802_%s.fits"
        cls.setup2()

class TestComm1803(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1803_%s.fits"
        cls.setup2()

class TestComm1804(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1804_%s.fits"
        cls.setup2()

class TestComm1805(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1805_%s.fits"
        cls.setup2()

class TestComm1806(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1806_%s.fits"
        cls.setup2()

class TestComm1807(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1807_%s.fits"
        cls.setup2()

class TestComm1808(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1808_%s.fits"
        cls.setup2()

class TestComm1809(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1809_%s.fits"
        cls.setup2()

class TestComm1810(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1810_%s.fits"
        cls.setup2()

class TestComm1811(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1811_%s.fits"
        cls.setup2()

class TestComm1812(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1812_%s.fits"
        cls.setup2()

class TestComm1813(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1813_%s.fits"
        cls.setup2()

class TestComm1814(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f845m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1814_%s.fits"
        cls.setup2()

class TestComm1815(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1815_%s.fits"
        cls.setup2()

class TestComm1816(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1816_%s.fits"
        cls.setup2()

class TestComm1817(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C1817_%s.fits"
        cls.setup2()

class TestComm1818(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C1818_%s.fits"
        cls.setup2()

class TestComm1819(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C1819_%s.fits"
        cls.setup2()

class TestComm1820(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1820_%s.fits"
        cls.setup2()

class TestComm1821(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1821_%s.fits"
        cls.setup2()

class TestComm1822(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1822_%s.fits"
        cls.setup2()

class TestComm1823(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f850lp"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1823_%s.fits"
        cls.setup2()

class TestComm1824(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1824_%s.fits"
        cls.setup2()

class TestComm1825(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1825_%s.fits"
        cls.setup2()

class TestComm1826(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,f953n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1826_%s.fits"
        cls.setup2()

class TestComm1827(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1827_%s.fits"
        cls.setup2()

class TestComm1828(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1828_%s.fits"
        cls.setup2()

class TestComm1829(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq232n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1829_%s.fits"
        cls.setup2()

class TestComm1830(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1830_%s.fits"
        cls.setup2()

class TestComm1831(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1831_%s.fits"
        cls.setup2()

class TestComm1832(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq243n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1832_%s.fits"
        cls.setup2()

class TestComm1833(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1833_%s.fits"
        cls.setup2()

class TestComm1834(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1834_%s.fits"
        cls.setup2()

class TestComm1835(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq378n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1835_%s.fits"
        cls.setup2()

class TestComm1836(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1836_%s.fits"
        cls.setup2()

class TestComm1837(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1837_%s.fits"
        cls.setup2()

class TestComm1838(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq387n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1838_%s.fits"
        cls.setup2()

class TestComm1839(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1839_%s.fits"
        cls.setup2()

class TestComm1840(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1840_%s.fits"
        cls.setup2()

class TestComm1841(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq422m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1841_%s.fits"
        cls.setup2()

class TestComm1842(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1842_%s.fits"
        cls.setup2()

class TestComm1843(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1843_%s.fits"
        cls.setup2()

class TestComm1844(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq436n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1844_%s.fits"
        cls.setup2()

class TestComm1845(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1845_%s.fits"
        cls.setup2()

class TestComm1846(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1846_%s.fits"
        cls.setup2()

class TestComm1847(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq437n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1847_%s.fits"
        cls.setup2()

class TestComm1848(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1848_%s.fits"
        cls.setup2()

class TestComm1849(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1849_%s.fits"
        cls.setup2()

class TestComm1850(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq492n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1850_%s.fits"
        cls.setup2()

class TestComm1851(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1851_%s.fits"
        cls.setup2()

class TestComm1852(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1852_%s.fits"
        cls.setup2()

class TestComm1853(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq508n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1853_%s.fits"
        cls.setup2()

class TestComm1854(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1854_%s.fits"
        cls.setup2()

class TestComm1855(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1855_%s.fits"
        cls.setup2()

class TestComm1856(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq575n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1856_%s.fits"
        cls.setup2()

class TestComm1857(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1857_%s.fits"
        cls.setup2()

class TestComm1858(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1858_%s.fits"
        cls.setup2()

class TestComm1859(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq619n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1859_%s.fits"
        cls.setup2()

class TestComm1860(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1860_%s.fits"
        cls.setup2()

class TestComm1861(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1861_%s.fits"
        cls.setup2()

class TestComm1862(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq634n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1862_%s.fits"
        cls.setup2()

class TestComm1863(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1863_%s.fits"
        cls.setup2()

class TestComm1864(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1864_%s.fits"
        cls.setup2()

class TestComm1865(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq672n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1865_%s.fits"
        cls.setup2()

class TestComm1866(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1866_%s.fits"
        cls.setup2()

class TestComm1867(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1867_%s.fits"
        cls.setup2()

class TestComm1868(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq674n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1868_%s.fits"
        cls.setup2()

class TestComm1869(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1869_%s.fits"
        cls.setup2()

class TestComm1870(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1870_%s.fits"
        cls.setup2()

class TestComm1871(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq727n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1871_%s.fits"
        cls.setup2()

class TestComm1872(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1872_%s.fits"
        cls.setup2()

class TestComm1873(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1873_%s.fits"
        cls.setup2()

class TestComm1874(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq750n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1874_%s.fits"
        cls.setup2()

class TestComm1875(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1875_%s.fits"
        cls.setup2()

class TestComm1876(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1876_%s.fits"
        cls.setup2()

class TestComm1877(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq889n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1877_%s.fits"
        cls.setup2()

class TestComm1878(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1878_%s.fits"
        cls.setup2()

class TestComm1879(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1879_%s.fits"
        cls.setup2()

class TestComm1880(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq906n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1880_%s.fits"
        cls.setup2()

class TestComm1881(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1881_%s.fits"
        cls.setup2()

class TestComm1882(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1882_%s.fits"
        cls.setup2()

class TestComm1883(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq924n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1883_%s.fits"
        cls.setup2()

class TestComm1884(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1884_%s.fits"
        cls.setup2()

class TestComm1885(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1885_%s.fits"
        cls.setup2()

class TestComm1886(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,fq937n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1886_%s.fits"
        cls.setup2()

class TestComm1887(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C1887_%s.fits"
        cls.setup2()

class TestComm1888(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C1888_%s.fits"
        cls.setup2()

class TestComm1889(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C1889_%s.fits"
        cls.setup2()

class TestComm1890(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C1890_%s.fits"
        cls.setup2()

class TestComm1891(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C1891_%s.fits"
        cls.setup2()

class TestComm1892(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C1892_%s.fits"
        cls.setup2()

class TestComm1893(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1893_%s.fits"
        cls.setup2()

class TestComm1894(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C1894_%s.fits"
        cls.setup2()

class TestComm1895(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C1895_%s.fits"
        cls.setup2()

class TestComm1896(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1896_%s.fits"
        cls.setup2()

class TestComm1897(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1897_%s.fits"
        cls.setup2()

class TestComm1898(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C1898_%s.fits"
        cls.setup2()

class TestComm1899(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C1899_%s.fits"
        cls.setup2()

class TestComm1900(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C1900_%s.fits"
        cls.setup2()

class TestComm1901(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C1901_%s.fits"
        cls.setup2()

class TestComm1902(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C1902_%s.fits"
        cls.setup2()

class TestComm1903(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C1903_%s.fits"
        cls.setup2()

class TestComm1904(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C1904_%s.fits"
        cls.setup2()

class TestComm1905(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1905_%s.fits"
        cls.setup2()

class TestComm1906(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1906_%s.fits"
        cls.setup2()

class TestComm1907(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1907_%s.fits"
        cls.setup2()

class TestComm1908(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1908_%s.fits"
        cls.setup2()

class TestComm1909(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1909_%s.fits"
        cls.setup2()

class TestComm1910(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1910_%s.fits"
        cls.setup2()

class TestComm1911(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1911_%s.fits"
        cls.setup2()

class TestComm1912(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C1912_%s.fits"
        cls.setup2()

class TestComm1913(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C1913_%s.fits"
        cls.setup2()

class TestComm1914(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C1914_%s.fits"
        cls.setup2()

class TestComm1915(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1915_%s.fits"
        cls.setup2()

class TestComm1916(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C1916_%s.fits"
        cls.setup2()

class TestComm1917(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C1917_%s.fits"
        cls.setup2()

class TestComm1918(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C1918_%s.fits"
        cls.setup2()

class TestComm1919(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C1919_%s.fits"
        cls.setup2()

class TestComm1920(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C1920_%s.fits"
        cls.setup2()

class TestComm1921(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C1921_%s.fits"
        cls.setup2()

class TestComm1922(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1922_%s.fits"
        cls.setup2()

class TestComm1923(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1923_%s.fits"
        cls.setup2()

class TestComm1924(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1924_%s.fits"
        cls.setup2()

class TestComm1925(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1925_%s.fits"
        cls.setup2()

class TestComm1926(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1926_%s.fits"
        cls.setup2()

class TestComm1927(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1927_%s.fits"
        cls.setup2()

class TestComm1928(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1928_%s.fits"
        cls.setup2()

class TestComm1929(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1929_%s.fits"
        cls.setup2()

class TestComm1930(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis1,g280,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1930_%s.fits"
        cls.setup2()

class TestComm1931(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1931_%s.fits"
        cls.setup2()

class TestComm1932(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f200lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1932_%s.fits"
        cls.setup2()

class TestComm1933(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f200lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1933_%s.fits"
        cls.setup2()

class TestComm1934(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1934_%s.fits"
        cls.setup2()

class TestComm1935(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f218w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1935_%s.fits"
        cls.setup2()

class TestComm1936(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f218w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1936_%s.fits"
        cls.setup2()

class TestComm1937(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1937_%s.fits"
        cls.setup2()

class TestComm1938(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1938_%s.fits"
        cls.setup2()

class TestComm1939(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,g),28.0,vegamag)"
        cls.fname="C1939_%s.fits"
        cls.setup2()

class TestComm1940(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,i),28.0,vegamag)"
        cls.fname="C1940_%s.fits"
        cls.setup2()

class TestComm1941(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,flam),box(5000.0,1.0),1.0e-18,flam)"
        cls.fname="C1941_%s.fits"
        cls.setup2()

class TestComm1942(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="rn(unit(1.0,fnu),band(sdss,z),28.0,vegamag)"
        cls.fname="C1942_%s.fits"
        cls.setup2()

class TestComm1943(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"
        cls.fname="C1943_%s.fits"
        cls.setup2()

class TestComm1944(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)*0.2+spec(el1302a.fits)*0.01333333333+spec(el1356a.fits)*0.012+spec(el2471a.fits)*0.01)"
        cls.fname="C1944_%s.fits"
        cls.setup2()

class TestComm1945(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1945_%s.fits"
        cls.setup2()

class TestComm1946(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f225w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))*2.0"
        cls.fname="C1946_%s.fits"
        cls.setup2()

class TestComm1947(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1947_%s.fits"
        cls.setup2()

class TestComm1948(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f275w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1948_%s.fits"
        cls.setup2()

class TestComm1949(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f275w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1949_%s.fits"
        cls.setup2()

class TestComm1950(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1950_%s.fits"
        cls.setup2()

class TestComm1951(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f280n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1951_%s.fits"
        cls.setup2()

class TestComm1952(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f280n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1952_%s.fits"
        cls.setup2()

class TestComm1953(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(cousins,r),28.0,vegamag)"
        cls.fname="C1953_%s.fits"
        cls.setup2()

class TestComm1954(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,i),28.0,vegamag)"
        cls.fname="C1954_%s.fits"
        cls.setup2()

class TestComm1955(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,j),28.0,vegamag)"
        cls.fname="C1955_%s.fits"
        cls.setup2()

class TestComm1956(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,k),28.0,vegamag)"
        cls.fname="C1956_%s.fits"
        cls.setup2()

class TestComm1957(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,r),28.0,vegamag)"
        cls.fname="C1957_%s.fits"
        cls.setup2()

class TestComm1958(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(bb(10000),band(johnson,u),28.0,vegamag)"
        cls.fname="C1958_%s.fits"
        cls.setup2()

class TestComm1959(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1959_%s.fits"
        cls.setup2()

class TestComm1960(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1960_%s.fits"
        cls.setup2()

class TestComm1961(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1961_%s.fits"
        cls.setup2()

class TestComm1962(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1962_%s.fits"
        cls.setup2()

class TestComm1963(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1963_%s.fits"
        cls.setup2()

class TestComm1964(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1964_%s.fits"
        cls.setup2()

class TestComm1965(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1965_%s.fits"
        cls.setup2()

class TestComm1966(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f300x"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1966_%s.fits"
        cls.setup2()

class TestComm1967(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1967_%s.fits"
        cls.setup2()

class TestComm1968(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f336w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1968_%s.fits"
        cls.setup2()

class TestComm1969(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f336w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1969_%s.fits"
        cls.setup2()

class TestComm1970(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1970_%s.fits"
        cls.setup2()

class TestComm1971(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f343n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1971_%s.fits"
        cls.setup2()

class TestComm1972(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f343n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1972_%s.fits"
        cls.setup2()

class TestComm1973(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1973_%s.fits"
        cls.setup2()

class TestComm1974(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f350lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1974_%s.fits"
        cls.setup2()

class TestComm1975(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f350lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1975_%s.fits"
        cls.setup2()

class TestComm1976(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1976_%s.fits"
        cls.setup2()

class TestComm1977(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f373n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1977_%s.fits"
        cls.setup2()

class TestComm1978(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f373n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1978_%s.fits"
        cls.setup2()

class TestComm1979(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1979_%s.fits"
        cls.setup2()

class TestComm1980(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1980_%s.fits"
        cls.setup2()

class TestComm1981(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1981_%s.fits"
        cls.setup2()

class TestComm1982(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1982_%s.fits"
        cls.setup2()

class TestComm1983(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1983_%s.fits"
        cls.setup2()

class TestComm1984(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f390w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1984_%s.fits"
        cls.setup2()

class TestComm1985(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1985_%s.fits"
        cls.setup2()

class TestComm1986(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1986_%s.fits"
        cls.setup2()

class TestComm1987(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f395n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1987_%s.fits"
        cls.setup2()

class TestComm1988(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1988_%s.fits"
        cls.setup2()

class TestComm1989(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1989_%s.fits"
        cls.setup2()

class TestComm1990(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f410m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1990_%s.fits"
        cls.setup2()

class TestComm1991(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1991_%s.fits"
        cls.setup2()

class TestComm1992(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1992_%s.fits"
        cls.setup2()

class TestComm1993(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f438w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1993_%s.fits"
        cls.setup2()

class TestComm1994(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1994_%s.fits"
        cls.setup2()

class TestComm1995(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1995_%s.fits"
        cls.setup2()

class TestComm1996(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f467m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1996_%s.fits"
        cls.setup2()

class TestComm1997(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C1997_%s.fits"
        cls.setup2()

class TestComm1998(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C1998_%s.fits"
        cls.setup2()

class TestComm1999(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f469n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C1999_%s.fits"
        cls.setup2()

class TestComm2000(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2000_%s.fits"
        cls.setup2()

class TestComm2001(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2001_%s.fits"
        cls.setup2()

class TestComm2002(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2002_%s.fits"
        cls.setup2()

class TestComm2003(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2003_%s.fits"
        cls.setup2()

class TestComm2004(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2004_%s.fits"
        cls.setup2()

class TestComm2005(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f475x"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2005_%s.fits"
        cls.setup2()

class TestComm2006(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2006_%s.fits"
        cls.setup2()

class TestComm2007(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2007_%s.fits"
        cls.setup2()

class TestComm2008(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f487n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2008_%s.fits"
        cls.setup2()

class TestComm2009(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2009_%s.fits"
        cls.setup2()

class TestComm2010(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2010_%s.fits"
        cls.setup2()

class TestComm2011(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="rn(unit(1.0,flam),band(sdss,r),28.0,vegamag)+em(5007.0,5.0,1.0E-13,flam)"
        cls.fname="C2011_%s.fits"
        cls.setup2()

class TestComm2012(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f502n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2012_%s.fits"
        cls.setup2()

class TestComm2013(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2013_%s.fits"
        cls.setup2()

class TestComm2014(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2014_%s.fits"
        cls.setup2()

class TestComm2015(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f547m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2015_%s.fits"
        cls.setup2()

class TestComm2016(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2016_%s.fits"
        cls.setup2()

class TestComm2017(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2017_%s.fits"
        cls.setup2()

class TestComm2018(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/agk_81d266_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C2018_%s.fits"
        cls.setup2()

class TestComm2019(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/alpha_lyr_stis_003.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C2019_%s.fits"
        cls.setup2()

class TestComm2020(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_28d4211_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2020_%s.fits"
        cls.setup2()

class TestComm2021(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/bd_75d325_stis_001.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C2021_%s.fits"
        cls.setup2()

class TestComm2022(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige110_stis_001.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C2022_%s.fits"
        cls.setup2()

class TestComm2023(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/feige34_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C2023_%s.fits"
        cls.setup2()

class TestComm2024(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C2024_%s.fits"
        cls.setup2()

class TestComm2025(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g93_48_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2025_%s.fits"
        cls.setup2()

class TestComm2026(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd108_005.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2026_%s.fits"
        cls.setup2()

class TestComm2027(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C2027_%s.fits"
        cls.setup2()

class TestComm2028(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd50_004.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2028_%s.fits"
        cls.setup2()

class TestComm2029(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C2029_%s.fits"
        cls.setup2()

class TestComm2030(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/grw_70d5824_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C2030_%s.fits"
        cls.setup2()

class TestComm2031(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz21_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2031_%s.fits"
        cls.setup2()

class TestComm2032(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz43_mod_004.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C2032_%s.fits"
        cls.setup2()

class TestComm2033(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz44_stis_001.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C2033_%s.fits"
        cls.setup2()

class TestComm2034(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/hz4_stis_001.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C2034_%s.fits"
        cls.setup2()

class TestComm2035(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lb227_004.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C2035_%s.fits"
        cls.setup2()

class TestComm2036(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/lds749b_mod_001.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2036_%s.fits"
        cls.setup2()

class TestComm2037(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/ngc7293_005.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C2037_%s.fits"
        cls.setup2()

class TestComm2038(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/sun_reference_stis_001.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2038_%s.fits"
        cls.setup2()

class TestComm2039(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(elliptical.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C2039_%s.fits"
        cls.setup2()

class TestComm2040(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(ngc1068_template.fits),0.05),band(johnson,b),28.0,vegamag)"
        cls.fname="C2040_%s.fits"
        cls.setup2()

class TestComm2041(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(orion.fits),0.25),band(johnson,b),28.0,vegamag)"
        cls.fname="C2041_%s.fits"
        cls.setup2()

class TestComm2042(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(orion_smooth.fits),0.15),band(johnson,b),28.0,vegamag)"
        cls.fname="C2042_%s.fits"
        cls.setup2()

class TestComm2043(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(pn_smooth.fits),0.1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2043_%s.fits"
        cls.setup2()

class TestComm2044(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(qso_template.fits),0.2),band(johnson,b),28.0,vegamag)"
        cls.fname="C2044_%s.fits"
        cls.setup2()

class TestComm2045(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="rn(z(spec(spiral.fits),0.3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2045_%s.fits"
        cls.setup2()

class TestComm2046(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f555w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2046_%s.fits"
        cls.setup2()

class TestComm2047(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2047_%s.fits"
        cls.setup2()

class TestComm2048(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f600lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2048_%s.fits"
        cls.setup2()

class TestComm2049(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f600lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2049_%s.fits"
        cls.setup2()

class TestComm2050(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2050_%s.fits"
        cls.setup2()

class TestComm2051(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2051_%s.fits"
        cls.setup2()

class TestComm2052(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2052_%s.fits"
        cls.setup2()

class TestComm2053(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2053_%s.fits"
        cls.setup2()

class TestComm2054(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2054_%s.fits"
        cls.setup2()

class TestComm2055(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,33000.,0.0,4.0)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C2055_%s.fits"
        cls.setup2()

class TestComm2056(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,3500,0.0,4.6)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2056_%s.fits"
        cls.setup2()

class TestComm2057(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,38000.,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2057_%s.fits"
        cls.setup2()

class TestComm2058(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,4060,0.0,4.5)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2058_%s.fits"
        cls.setup2()

class TestComm2059(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,44500,0.0,5.0)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2059_%s.fits"
        cls.setup2()

class TestComm2060(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,4560,0.0,4.5)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2060_%s.fits"
        cls.setup2()

class TestComm2061(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,4850,0.0,1.1)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2061_%s.fits"
        cls.setup2()

class TestComm2062(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5250,0.0,4.5)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C2062_%s.fits"
        cls.setup2()

class TestComm2063(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5570,0.0,4.5)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2063_%s.fits"
        cls.setup2()

class TestComm2064(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5770,0.0,4.5)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2064_%s.fits"
        cls.setup2()

class TestComm2065(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,5860,0.0,4.4)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2065_%s.fits"
        cls.setup2()

class TestComm2066(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,6200,0.0,4.4)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2066_%s.fits"
        cls.setup2()

class TestComm2067(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,6440,0.0,4.3)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C2067_%s.fits"
        cls.setup2()

class TestComm2068(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,6890,0.0,4.3)*ebmvx(0.2,lmc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2068_%s.fits"
        cls.setup2()

class TestComm2069(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,7200,0.0,4.3)*ebmvx(0.16,smc),band(johnson,b),28.0,vegamag)"
        cls.fname="C2069_%s.fits"
        cls.setup2()

class TestComm2070(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,7700,0.0,1.7)*ebmvx(0.12,gal3),band(johnson,b),28.0,vegamag)"
        cls.fname="C2070_%s.fits"
        cls.setup2()

class TestComm2071(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,8200,0.0,4.3)*ebmvx(0.08,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2071_%s.fits"
        cls.setup2()

class TestComm2072(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,8720,0.0,4.2)*ebmvx(0.04,gal1),band(johnson,b),28.0,vegamag)"
        cls.fname="C2072_%s.fits"
        cls.setup2()

class TestComm2073(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),28.0,vegamag)"
        cls.fname="C2073_%s.fits"
        cls.setup2()

class TestComm2074(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2074_%s.fits"
        cls.setup2()

class TestComm2075(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2075_%s.fits"
        cls.setup2()

class TestComm2076(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f606w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2076_%s.fits"
        cls.setup2()

class TestComm2077(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2077_%s.fits"
        cls.setup2()

class TestComm2078(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f621m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2078_%s.fits"
        cls.setup2()

class TestComm2079(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f621m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2079_%s.fits"
        cls.setup2()

class TestComm2080(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2080_%s.fits"
        cls.setup2()

class TestComm2081(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f625w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2081_%s.fits"
        cls.setup2()

class TestComm2082(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f625w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2082_%s.fits"
        cls.setup2()

class TestComm2083(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2083_%s.fits"
        cls.setup2()

class TestComm2084(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f631n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2084_%s.fits"
        cls.setup2()

class TestComm2085(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f631n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2085_%s.fits"
        cls.setup2()

class TestComm2086(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2086_%s.fits"
        cls.setup2()

class TestComm2087(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f645n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2087_%s.fits"
        cls.setup2()

class TestComm2088(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f645n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2088_%s.fits"
        cls.setup2()

class TestComm2089(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2089_%s.fits"
        cls.setup2()

class TestComm2090(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f656n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2090_%s.fits"
        cls.setup2()

class TestComm2091(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f656n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2091_%s.fits"
        cls.setup2()

class TestComm2092(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2092_%s.fits"
        cls.setup2()

class TestComm2093(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f657n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2093_%s.fits"
        cls.setup2()

class TestComm2094(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f657n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2094_%s.fits"
        cls.setup2()

class TestComm2095(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2095_%s.fits"
        cls.setup2()

class TestComm2096(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f658n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2096_%s.fits"
        cls.setup2()

class TestComm2097(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f658n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2097_%s.fits"
        cls.setup2()

class TestComm2098(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2098_%s.fits"
        cls.setup2()

class TestComm2099(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f665n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2099_%s.fits"
        cls.setup2()

class TestComm2100(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f665n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2100_%s.fits"
        cls.setup2()

class TestComm2101(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2101_%s.fits"
        cls.setup2()

class TestComm2102(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f673n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2102_%s.fits"
        cls.setup2()

class TestComm2103(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f673n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2103_%s.fits"
        cls.setup2()

class TestComm2104(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2104_%s.fits"
        cls.setup2()

class TestComm2105(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f680n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2105_%s.fits"
        cls.setup2()

class TestComm2106(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f680n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2106_%s.fits"
        cls.setup2()

class TestComm2107(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2107_%s.fits"
        cls.setup2()

class TestComm2108(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f689m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2108_%s.fits"
        cls.setup2()

class TestComm2109(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f689m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2109_%s.fits"
        cls.setup2()

class TestComm2110(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2110_%s.fits"
        cls.setup2()

class TestComm2111(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f763m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2111_%s.fits"
        cls.setup2()

class TestComm2112(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f763m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2112_%s.fits"
        cls.setup2()

class TestComm2113(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2113_%s.fits"
        cls.setup2()

class TestComm2114(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f775w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2114_%s.fits"
        cls.setup2()

class TestComm2115(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f775w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2115_%s.fits"
        cls.setup2()

class TestComm2116(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2116_%s.fits"
        cls.setup2()

class TestComm2117(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2117_%s.fits"
        cls.setup2()

class TestComm2118(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2118_%s.fits"
        cls.setup2()

class TestComm2119(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2119_%s.fits"
        cls.setup2()

class TestComm2120(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2120_%s.fits"
        cls.setup2()

class TestComm2121(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2121_%s.fits"
        cls.setup2()

class TestComm2122(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2122_%s.fits"
        cls.setup2()

class TestComm2123(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2123_%s.fits"
        cls.setup2()

class TestComm2124(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2124_%s.fits"
        cls.setup2()

class TestComm2125(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2125_%s.fits"
        cls.setup2()

class TestComm2126(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_100.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2126_%s.fits"
        cls.setup2()

class TestComm2127(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2127_%s.fits"
        cls.setup2()

class TestComm2128(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2128_%s.fits"
        cls.setup2()

class TestComm2129(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_114.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2129_%s.fits"
        cls.setup2()

class TestComm2130(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_117.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2130_%s.fits"
        cls.setup2()

class TestComm2131(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_118.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2131_%s.fits"
        cls.setup2()

class TestComm2132(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2132_%s.fits"
        cls.setup2()

class TestComm2133(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2133_%s.fits"
        cls.setup2()

class TestComm2134(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_13.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2134_%s.fits"
        cls.setup2()

class TestComm2135(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2135_%s.fits"
        cls.setup2()

class TestComm2136(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2136_%s.fits"
        cls.setup2()

class TestComm2137(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_15.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2137_%s.fits"
        cls.setup2()

class TestComm2138(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2138_%s.fits"
        cls.setup2()

class TestComm2139(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_16.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2139_%s.fits"
        cls.setup2()

class TestComm2140(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2140_%s.fits"
        cls.setup2()

class TestComm2141(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_17.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2141_%s.fits"
        cls.setup2()

class TestComm2142(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2142_%s.fits"
        cls.setup2()

class TestComm2143(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_18.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2143_%s.fits"
        cls.setup2()

class TestComm2144(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2144_%s.fits"
        cls.setup2()

class TestComm2145(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_19.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2145_%s.fits"
        cls.setup2()

class TestComm2146(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2146_%s.fits"
        cls.setup2()

class TestComm2147(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2147_%s.fits"
        cls.setup2()

class TestComm2148(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2148_%s.fits"
        cls.setup2()

class TestComm2149(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_20.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2149_%s.fits"
        cls.setup2()

class TestComm2150(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_22.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2150_%s.fits"
        cls.setup2()

class TestComm2151(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_23.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2151_%s.fits"
        cls.setup2()

class TestComm2152(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_24.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2152_%s.fits"
        cls.setup2()

class TestComm2153(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_25.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2153_%s.fits"
        cls.setup2()

class TestComm2154(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_26.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2154_%s.fits"
        cls.setup2()

class TestComm2155(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_27.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2155_%s.fits"
        cls.setup2()

class TestComm2156(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_29.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2156_%s.fits"
        cls.setup2()

class TestComm2157(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2157_%s.fits"
        cls.setup2()

class TestComm2158(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_31.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2158_%s.fits"
        cls.setup2()

class TestComm2159(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_33.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2159_%s.fits"
        cls.setup2()

class TestComm2160(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_34.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2160_%s.fits"
        cls.setup2()

class TestComm2161(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_36.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2161_%s.fits"
        cls.setup2()

class TestComm2162(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_37.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2162_%s.fits"
        cls.setup2()

class TestComm2163(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_38.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2163_%s.fits"
        cls.setup2()

class TestComm2164(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2164_%s.fits"
        cls.setup2()

class TestComm2165(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_40.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2165_%s.fits"
        cls.setup2()

class TestComm2166(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2166_%s.fits"
        cls.setup2()

class TestComm2167(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2167_%s.fits"
        cls.setup2()

class TestComm2168(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_50.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2168_%s.fits"
        cls.setup2()

class TestComm2169(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_51.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2169_%s.fits"
        cls.setup2()

class TestComm2170(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_52.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2170_%s.fits"
        cls.setup2()

class TestComm2171(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_53.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2171_%s.fits"
        cls.setup2()

class TestComm2172(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_54.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2172_%s.fits"
        cls.setup2()

class TestComm2173(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_55.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2173_%s.fits"
        cls.setup2()

class TestComm2174(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_56.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2174_%s.fits"
        cls.setup2()

class TestComm2175(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2175_%s.fits"
        cls.setup2()

class TestComm2176(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_60.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2176_%s.fits"
        cls.setup2()

class TestComm2177(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2177_%s.fits"
        cls.setup2()

class TestComm2178(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_63.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2178_%s.fits"
        cls.setup2()

class TestComm2179(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2179_%s.fits"
        cls.setup2()

class TestComm2180(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2180_%s.fits"
        cls.setup2()

class TestComm2181(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_65.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2181_%s.fits"
        cls.setup2()

class TestComm2182(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2182_%s.fits"
        cls.setup2()

class TestComm2183(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_67.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2183_%s.fits"
        cls.setup2()

class TestComm2184(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_69.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2184_%s.fits"
        cls.setup2()

class TestComm2185(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_76.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2185_%s.fits"
        cls.setup2()

class TestComm2186(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_87.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2186_%s.fits"
        cls.setup2()

class TestComm2187(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2187_%s.fits"
        cls.setup2()

class TestComm2188(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_93.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2188_%s.fits"
        cls.setup2()

class TestComm2189(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_95.fits),band(cousins,i),28.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2189_%s.fits"
        cls.setup2()

class TestComm2190(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f814w"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2190_%s.fits"
        cls.setup2()

class TestComm2191(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2191_%s.fits"
        cls.setup2()

class TestComm2192(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f845m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2192_%s.fits"
        cls.setup2()

class TestComm2193(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f845m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2193_%s.fits"
        cls.setup2()

class TestComm2194(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2194_%s.fits"
        cls.setup2()

class TestComm2195(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2195_%s.fits"
        cls.setup2()

class TestComm2196(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),28.0,vegamag)"
        cls.fname="C2196_%s.fits"
        cls.setup2()

class TestComm2197(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),28.0,vegamag)"
        cls.fname="C2197_%s.fits"
        cls.setup2()

class TestComm2198(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),28.0,vegamag)"
        cls.fname="C2198_%s.fits"
        cls.setup2()

class TestComm2199(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2199_%s.fits"
        cls.setup2()

class TestComm2200(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2200_%s.fits"
        cls.setup2()

class TestComm2201(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2201_%s.fits"
        cls.setup2()

class TestComm2202(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f850lp"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2202_%s.fits"
        cls.setup2()

class TestComm2203(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2203_%s.fits"
        cls.setup2()

class TestComm2204(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f953n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2204_%s.fits"
        cls.setup2()

class TestComm2205(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,f953n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2205_%s.fits"
        cls.setup2()

class TestComm2206(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2206_%s.fits"
        cls.setup2()

class TestComm2207(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq232n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2207_%s.fits"
        cls.setup2()

class TestComm2208(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq232n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2208_%s.fits"
        cls.setup2()

class TestComm2209(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2209_%s.fits"
        cls.setup2()

class TestComm2210(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq243n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2210_%s.fits"
        cls.setup2()

class TestComm2211(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq243n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2211_%s.fits"
        cls.setup2()

class TestComm2212(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2212_%s.fits"
        cls.setup2()

class TestComm2213(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq378n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2213_%s.fits"
        cls.setup2()

class TestComm2214(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq378n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2214_%s.fits"
        cls.setup2()

class TestComm2215(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2215_%s.fits"
        cls.setup2()

class TestComm2216(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq387n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2216_%s.fits"
        cls.setup2()

class TestComm2217(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq387n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2217_%s.fits"
        cls.setup2()

class TestComm2218(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2218_%s.fits"
        cls.setup2()

class TestComm2219(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq422m"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2219_%s.fits"
        cls.setup2()

class TestComm2220(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq422m"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2220_%s.fits"
        cls.setup2()

class TestComm2221(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2221_%s.fits"
        cls.setup2()

class TestComm2222(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq436n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2222_%s.fits"
        cls.setup2()

class TestComm2223(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq436n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2223_%s.fits"
        cls.setup2()

class TestComm2224(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2224_%s.fits"
        cls.setup2()

class TestComm2225(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq437n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2225_%s.fits"
        cls.setup2()

class TestComm2226(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq437n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2226_%s.fits"
        cls.setup2()

class TestComm2227(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2227_%s.fits"
        cls.setup2()

class TestComm2228(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq492n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2228_%s.fits"
        cls.setup2()

class TestComm2229(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq492n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2229_%s.fits"
        cls.setup2()

class TestComm2230(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2230_%s.fits"
        cls.setup2()

class TestComm2231(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq508n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2231_%s.fits"
        cls.setup2()

class TestComm2232(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq508n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2232_%s.fits"
        cls.setup2()

class TestComm2233(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2233_%s.fits"
        cls.setup2()

class TestComm2234(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq575n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2234_%s.fits"
        cls.setup2()

class TestComm2235(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq575n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2235_%s.fits"
        cls.setup2()

class TestComm2236(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2236_%s.fits"
        cls.setup2()

class TestComm2237(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq619n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2237_%s.fits"
        cls.setup2()

class TestComm2238(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq619n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2238_%s.fits"
        cls.setup2()

class TestComm2239(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2239_%s.fits"
        cls.setup2()

class TestComm2240(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq634n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2240_%s.fits"
        cls.setup2()

class TestComm2241(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq634n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2241_%s.fits"
        cls.setup2()

class TestComm2242(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2242_%s.fits"
        cls.setup2()

class TestComm2243(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq672n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2243_%s.fits"
        cls.setup2()

class TestComm2244(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq672n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2244_%s.fits"
        cls.setup2()

class TestComm2245(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2245_%s.fits"
        cls.setup2()

class TestComm2246(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq674n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2246_%s.fits"
        cls.setup2()

class TestComm2247(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq674n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2247_%s.fits"
        cls.setup2()

class TestComm2248(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2248_%s.fits"
        cls.setup2()

class TestComm2249(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq727n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2249_%s.fits"
        cls.setup2()

class TestComm2250(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq727n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2250_%s.fits"
        cls.setup2()

class TestComm2251(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2251_%s.fits"
        cls.setup2()

class TestComm2252(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq750n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2252_%s.fits"
        cls.setup2()

class TestComm2253(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq750n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2253_%s.fits"
        cls.setup2()

class TestComm2254(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2254_%s.fits"
        cls.setup2()

class TestComm2255(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq889n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2255_%s.fits"
        cls.setup2()

class TestComm2256(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq889n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2256_%s.fits"
        cls.setup2()

class TestComm2257(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2257_%s.fits"
        cls.setup2()

class TestComm2258(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq906n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2258_%s.fits"
        cls.setup2()

class TestComm2259(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq906n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2259_%s.fits"
        cls.setup2()

class TestComm2260(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2260_%s.fits"
        cls.setup2()

class TestComm2261(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq924n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2261_%s.fits"
        cls.setup2()

class TestComm2262(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq924n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2262_%s.fits"
        cls.setup2()

class TestComm2263(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),22.0,vegamag)"
        cls.fname="C2263_%s.fits"
        cls.setup2()

class TestComm2264(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq937n"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),28.0,vegamag)"
        cls.fname="C2264_%s.fits"
        cls.setup2()

class TestComm2265(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,fq937n"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2265_%s.fits"
        cls.setup2()

class TestComm2266(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(cousins,r),23.0,vegamag)"
        cls.fname="C2266_%s.fits"
        cls.setup2()

class TestComm2267(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,i),23.0,vegamag)"
        cls.fname="C2267_%s.fits"
        cls.setup2()

class TestComm2268(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,j),23.0,vegamag)"
        cls.fname="C2268_%s.fits"
        cls.setup2()

class TestComm2269(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,k),23.0,vegamag)"
        cls.fname="C2269_%s.fits"
        cls.setup2()

class TestComm2270(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,r),23.0,vegamag)"
        cls.fname="C2270_%s.fits"
        cls.setup2()

class TestComm2271(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(bb(10000),band(johnson,u),23.0,vegamag)"
        cls.fname="C2271_%s.fits"
        cls.setup2()

class TestComm2272(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,11900,0.0,4.0)*ebmvx(0.2,lmc),band(johnson,b),23.0,vegamag)"
        cls.fname="C2272_%s.fits"
        cls.setup2()

class TestComm2273(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,15400,0.0,3.9)*ebmvx(0.16,smc),band(johnson,b),23.0,vegamag)"
        cls.fname="C2273_%s.fits"
        cls.setup2()

class TestComm2274(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,18700,0.0,3.9)*ebmvx(0.12,gal3),band(johnson,b),23.0,vegamag)"
        cls.fname="C2274_%s.fits"
        cls.setup2()

class TestComm2275(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,25400,0.0,3.9)*ebmvx(0.08,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2275_%s.fits"
        cls.setup2()

class TestComm2276(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,30000,0.0,4.0)*ebmvx(0.04,gal1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2276_%s.fits"
        cls.setup2()

class TestComm2277(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1)*ebmvx(0.24,xgal),band(johnson,b),23.0,vegamag)"
        cls.fname="C2277_%s.fits"
        cls.setup2()

class TestComm2278(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),17.0,vegamag)"
        cls.fname="C2278_%s.fits"
        cls.setup2()

class TestComm2279(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),18.0,vegamag)"
        cls.fname="C2279_%s.fits"
        cls.setup2()

class TestComm2280(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(icat(k93models,9230,0.0,4.1),band(johnson,v),23.0,vegamag)"
        cls.fname="C2280_%s.fits"
        cls.setup2()

class TestComm2281(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(Bessell,j),23.0,vegamag)"
        cls.fname="C2281_%s.fits"
        cls.setup2()

class TestComm2282(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,h),23.0,vegamag)"
        cls.fname="C2282_%s.fits"
        cls.setup2()

class TestComm2283(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(pl(4000.0,-2.0,flam),band(bessell,k),23.0,vegamag)"
        cls.fname="C2283_%s.fits"
        cls.setup2()

class TestComm2284(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2284_%s.fits"
        cls.setup2()

class TestComm2285(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_1.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2285_%s.fits"
        cls.setup2()

class TestComm2286(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_10.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2286_%s.fits"
        cls.setup2()

class TestComm2287(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_11.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2287_%s.fits"
        cls.setup2()

class TestComm2288(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_12.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2288_%s.fits"
        cls.setup2()

class TestComm2289(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_14.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2289_%s.fits"
        cls.setup2()

class TestComm2290(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2290_%s.fits"
        cls.setup2()

class TestComm2291(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_2.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.16,smc)"
        cls.fname="C2291_%s.fits"
        cls.setup2()

class TestComm2292(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_3.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.2,lmc)"
        cls.fname="C2292_%s.fits"
        cls.setup2()

class TestComm2293(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_4.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.24,xgal)"
        cls.fname="C2293_%s.fits"
        cls.setup2()

class TestComm2294(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2294_%s.fits"
        cls.setup2()

class TestComm2295(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_5.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.08,gal1)"
        cls.fname="C2295_%s.fits"
        cls.setup2()

class TestComm2296(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_6.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.12,gal3)"
        cls.fname="C2296_%s.fits"
        cls.setup2()

class TestComm2297(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(spec(/grp/hst/cdbs//grid/pickles/dat_uvk/pickles_uk_9.fits),band(cousins,i),23.0,vegamag)*ebmvx(0.04,gal1)"
        cls.fname="C2297_%s.fits"
        cls.setup2()

class TestComm2298(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/g191b2b_mod_004.fits),0.05),band(johnson,b),23.0,vegamag)"
        cls.fname="C2298_%s.fits"
        cls.setup2()

class TestComm2299(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd153_mod_004.fits),0.1),band(johnson,b),23.0,vegamag)"
        cls.fname="C2299_%s.fits"
        cls.setup2()

class TestComm2300(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280"
        cls.spectrum="rn(z(spec(/grp/hst/cdbs//calspec/gd71_mod_005.fits),0.15),band(johnson,b),23.0,vegamag)"
        cls.fname="C2300_%s.fits"
        cls.setup2()

class TestComm2301(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2301_%s.fits"
        cls.setup2()

class TestComm2302(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),21.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2302_%s.fits"
        cls.setup2()

class TestComm2303(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.1,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2303_%s.fits"
        cls.setup2()

class TestComm2304(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.424602593467696,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2304_%s.fits"
        cls.setup2()

class TestComm2305(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2305_%s.fits"
        cls.setup2()

class TestComm2306(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),23.3,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2306_%s.fits"
        cls.setup2()

class TestComm2307(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*0.5+spec(Zodi.fits)*0.5+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2307_%s.fits"
        cls.setup2()

class TestComm2308(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)*2.0+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2308_%s.fits"
        cls.setup2()

class TestComm2309(conv_base.ParentCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="wfc3,uvis2,g280,bkg"
        cls.spectrum="spec(earthshine.fits)+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)+(spec(el1215a.fits)+spec(el1302a.fits)+spec(el1356a.fits)+spec(el2471a.fits))"
        cls.fname="C2309_%s.fits"
        cls.setup2()

