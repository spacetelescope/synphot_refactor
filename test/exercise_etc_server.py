from __future__ import division
"""

At present, this test suite does not compare results to reference values.
It runs one each of the following typical ETC use cases in server/client mode:
  calcphot
  countrate
  thermback
  SpecSourceRate (like countrate but also returns resulting spectrum)
  calcspec

(Note that these do NOT correspond to the synphot tasks of the same name.
They provide only stripped-down functionality necessary to run the ETC with
all the usual defaults set. Almost all the parameters provided in the synphot
call are ignored. See the relevant calculator classes in the etc.py module for
more detail.)

In order to run this test suite, you must first have started the server by
running the pysynphot file server.py. This will start the server,
which will run indefinitely.
The server prints diagnostic output to stdout, so it is useful to start this
in a specific window, in which you must first:
  - Define PYSYN_CDBS
  - cd to a directory that contains the files earthshine.fits and Zodi.fits
  
Then you can run this module from the shell in the usual way, eg:

gaudete> python /data/gaudete1/laidler/pyinstall/pysynphot/etc_test.py

If you get a "Connection refused" message, it probably means there is
no server running, and you need to start it as described above.

Standard output from a sample run resembles the following:

gaudete> python /data/gaudete1/laidler/pyinstall/pysynphot/etc_test.py

==============================================
Client connected to server.
Client sent:   calcphot&spectrum="rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)"&obsmode="acs,hrc,F220W"

==============================================
Client connected to server.
Client sent:   calcspec&spectrum="rn(pl(4000.0,-1.0,flam),box(1500,1.0),1.00E-14,flam)"&output="/data/gaudete1/laidler/ssb/astrolib_aux/pysynphot_userdata/specAV1.fits"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"

==============================================
Client connected to server.
Client sent:   SpecSourcerateSpec&spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"&instrument="wfc3,uvis1,g280"&output="/data/gaudete1/laidler/ssb/astrolib_aux/pysynphot_userdata/specOB1.fits"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"

==============================================
Client connected to server.
Client sent:   countrate&spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"&instrument="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"

==============================================
Client connected to server.
Client sent:   thermback&obsmode="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"

==============================================
 Client sent: calcphot&spectrum="rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)"&obsmode="acs,hrc,F220W"
 Client received: 2330.22324316

==============================================
 Client sent: calcspec&spectrum="rn(pl(4000.0,-1.0,flam),box(1500,1.0),1.00E-14,flam)"&output="/data/gaudete1/laidler/ssb/astrolib_aux/pysynphot_userdata/specAV1.fits"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"
 Client received: Power law: refwave 4000.000000, index -1.000000 * <pysynphot.spectrum.UniformTransmission object at 0xb5cf26ac>

==============================================
 Client sent: SpecSourcerateSpec&spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"&instrument="wfc3,uvis1,g280"&output="/data/gaudete1/laidler/ssb/astrolib_aux/pysynphot_userdata/specOB1.fits"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"
 Client received: 7869.69749379;/data/gaudete1/laidler/ssb/astrolib_aux/pysynphot_userdata/specOB1.fits

==============================================
 Client sent: countrate&spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"&instrument="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"
 Client received: (65.9137435293, 11399.121714437108)

==============================================
 Client sent: thermback&obsmode="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"
 Client received: 0.0304315556327


The corresponding output in the server window for the same run (if running
in debug mode):

Server connected from ('127.0.0.1', 58512)
Server connected from ('127.0.0.1', 58513)
Server connected from ('127.0.0.1', 58514)
Server connected from ('127.0.0.1', 58515)
Server connected from ('127.0.0.1', 58516)
elapsed time in calcphot:  1.7571079731 sec.  obsmode is: acs,hrc,F220W
Server disconnected from ('127.0.0.1', 58512)
elapsed time in calcspec:  0.452430963516 sec.  spectrum is: rn(pl(4000.0,-1.0,flam),box(1500,1.0),1.00E-14,flam)
Server disconnected from ('127.0.0.1', 58513)
elapsed time:  1.21769523621 sec.  obsmode is: wfc3,uvis1,g280
Server disconnected from ('127.0.0.1', 58514)
elapsed time in calcphot:  1.4881978035 sec.  obsmode is: wfc3,ir,f110w
Server disconnected from ('127.0.0.1', 58515)
elapsed time in calcphot:  2.85065197945 sec.  obsmode is: wfc3,ir,f110w
Server disconnected from ('127.0.0.1', 58516)


Debug mode is controlled by the etc.debug setting in *this* module.
"""
import os
import socket
import threading
import SocketServer
from pysynphot.client import Client

#Places used by test code
userdir   = os.environ['PYSYN_USERDATA']

from pysynphot import etc
etc.debug = 1

def test():
    cl1 = Client ('localhost',\
        'calcphot&spectrum="rn(unit(1,flam),box(5500.0,1),1.0E-18,flam)"&obsmode="acs,hrc,F220W"')
    cl1.run()

    cl2 = Client ('localhost',\
        'countrate&spectrum="spec(earthshine.fits)*0.5+rn(spec(Zodi.fits),band(johnson,v),22.7,vegamag)"&instrument="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"')
    cl2.run()

    cl3 = Client ('localhost',\
        'thermback&obsmode="wfc3,ir,f110w"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"')
    cl3.run()

    outfile = os.path.join(userdir,'specOB1.fits')

    cl4 = Client ('localhost',\
        'SpecSourcerateSpec&spectrum="rn(unit(1.0,flam),band(johnson,v),15,vegamag)"&instrument="wfc3,uvis1,g280"&output="%s"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"'%outfile)
    cl4.run()

    outfile = os.path.join(userdir,'specAV1.fits')
    cl5 = Client ('localhost',\
                  'calcspec&spectrum="rn(pl(4000.0,-1.0,flam),box(1500,1.0),1.00E-14,flam)"&output="%s"&area="45238.93416"&mode="a"&grtbl="mtab$*_tmg.fits"&cmptbl="mtab$*_tmc.fits"'%outfile)
    cl5.run()

    cl6 = Client('localhost',
                 'showfiles&obsmode="acs,hrc,f555w"&output="testme.txt"')
    cl6.run()

    cl7 = Client('localhost','ping')
    cl7.run()
    
    cl8 = Client('localhost','quit')
    cl8.run()
    
if __name__ == '__main__':
    test()

