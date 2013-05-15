import sys,os
import sqlite3

def run():
    """ Generate TestCases from cmdfile according to the pattern in patternfile"""
    #Define the import statements
    impheader = """import sys
import conv_base

"""
    #Define the test case pattern
    pattern="""class Test%d(conv_base.%sCase):
    @classmethod
    def setUpClass(cls):
        cls.obsmode="%s"
        cls.spectrum="%s"
        cls.fname="C%s_%s.fits"
        cls.setup2()\n\n"""


    #We're going to split these by obsmode.
    outfiles = {'None':'sponly/sponly.py',
                'acs':'acs/acs.py',
                'nicmos':'nicmos/nicmos.py',
                'stis':'stis/stis.py',
                'wfc3,ir':'wfc3_ir/wfc3_ir.py',
                'wfc3,uvis1':'wfc3_uvis1/wfc3_uvis1.py',
                'wfc3,uvis2':'wfc3_uvis2/wfc3_uvis2.py',
                'oops':'oops/oops.py'
                }

    #And subclass for spectrum-only and thermal cases based on obsmode.
    casetype = {"None": "Spec",
                "nicmos": "Therm",
                "wfc3,ir": "Therm"}
    #Use with default=Comm
                
    #Open the database
    db = sqlite3.connect("/ssbwebv1/data1/pandokia/old/pdk/c3/db/pdk.db")


    #Open and initialize the output files
    setdirs(outfiles)
    for k in outfiles:
        outfiles[k] = open(outfiles[k], 'w')
        outfiles[k].write(impheader)

    count=0

    #Select unique (obsmode,spectrum) pairs from our database table of
    #commissioning tests. Sort them by obsmode.

    #Omit cases where spectrum is None, because we've verified that all
    #those obsmodes are duplicated elsewhere.

    #First the bp only. The purpose of these is thermal.
    c = db.execute(""" SELECT DISTINCT obsmode, spectrum
                       FROM synpysyn
                       WHERE spectrum != "None"
                       ORDER BY obsmode""")

    #Now loop over them, and define test cases.
    for x in c:
       obsmode, spectrum = x
       count+=1
       outkey=pickname(obsmode,outfiles)
       defn=pattern%(count,
                     casetype.get(outkey, "Comm"),
                     obsmode,spectrum,count,"%s")
       outfiles[outkey].write(defn)

    #Close all the files
    for k in outfiles:
        outfiles[k].close()

def setdirs(outfiles):
    """Create the directories if need be"""
    for k in outfiles:
        fname=outfiles[k]
        dname= os.path.dirname(fname)
        if not os.path.isdir(dname):
            os.mkdir(dname)

def pickname(obsmode, outfiles):
    """The obsmode string starts with one of the keys of outfiles.
    Pick the right one and return it."""

    for k in outfiles:
        if obsmode.startswith(k):
            return k

    return 'oops'
            
if __name__ == '__main__':
    run()
    
