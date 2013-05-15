from __future__ import division
import os, sys
import pysynphot as S
from pysynphot import wavetable
import testutil

## TO RUN IN A SINGLE TEST IN DEBUG MODE:
## import tickettest
## tickettest.FileTestCase('testwave').debug()

class WavecatTestCase(testutil.FPTestCase):
    def setUp(self):
        self.w=wavetable.wavetable

    def testmatch(self):
        "tickettest.WavecatTestCase('testmatch'): nicmos,3,f220m"
        obs='nicmos,3,f220m'
        self.assertEqual(self.w[obs],'(7000.0,29996.0,1.0)')

    def testend(self):
        "tickettest WavecatTestCase('testend'): Ticket #20: acs,hrc,f550m"
        obs="acs,hrc,f550m"
        self.assertEqual(self.w[obs],self.w['acs,hrc'])

    def testmiddle1(self):
        "tickettest.WavecatTestCase('testmiddle1'): Ticket #37, stis,ccd,g750m"
        obs='stis,ccd,g750m'
        self.assertEqual(self.w[obs],self.w['stis,g750m'])

    def testmiddle2(self):
        "tickettest.WavecatTestCase('testmiddle2'): Ticket #37, stis,fuvmama,g140l,s52x2"
        obs='stis,fuvmama,g140l,s52x2'
        self.assertEqual(self.w[obs],self.w['stis,g140l'])

    def testmissing(self):
        "tickettest.WavecatTestCase('testmissing'): #37, johnson,v"
        obs='johnson,v'
        self.assertRaises(KeyError,self.w.__getitem__,obs)

    def testambig(self):
        "tickettest.WavecatTestCase('testambig'): #37, stis,nuvmama,e230h,c2263,s02x02"
        obs="stis,nuvmama,e230h,c2263,s02x02"
        self.assertEqual(self.w[obs],self.w['stis,e230h,c2263'])

               
if __name__ == '__main__':
    if 'debug' in sys.argv:
        testutil.debug(__name__)
    else:
        testutil.testall(__name__,2)
