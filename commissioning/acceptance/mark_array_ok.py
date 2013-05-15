"""I have also noticed a trend in a number of the failed cases that
involve array comparisons: the mean discrepancy is very small,
and there are a small number of significant outliers. At present,
such a test fails the rigorous criteria we are using. However,
I am thinking of writing a utility to identify these cases and
mark them as acceptable failures. Any comments/objections?


Basic idea:
  - look for failed tests, possibly only of the array types
  - for each test,
     extract tra_discrepmean, tra_outliers, tda_sigthresh
     if abs(mean)<sigthresh and outliers<something,
        set attn=N
        print something to stdout

"""
import sqlite3
import time, sys

def run(test_run,maxoutliers=50,maxdev=0.015):

    #Connect to the DB
    db = sqlite3.connect("/aten/data1/ssb/test/stf/cgi/db/stf.db")
    idlist=[]

    #Pick out the failed tests from the test run
    ctr = db.execute("""SELECT result_scalar.key_id, result_scalar.test_name
                      FROM result_scalar
                      WHERE result_scalar.test_run = ?
                      AND result_scalar.status = 'F'
                      AND project = 'syn_pysyn'
                      AND host = 'gaudete' """,(test_run,))

    #Loop over the tests to pick out the ones we want to analyze
    for x in ctr:
        key,name=x
        if "testcr" in name: #then it's an array test; carry on.
            ctra = db.execute("""SELECT result_tra.value
                         FROM result_tra
                         WHERE result_tra.key_id = ?
                         AND   result_tra.name = 'discrepmean'""",
                          (key,))

            for xx in ctra:
                discrepmean=float(xx[0])
                
                ctra2 = db.execute("""SELECT result_tra.value
                         FROM result_tra
                         WHERE result_tra.key_id = ?
                         AND   result_tra.name = 'outliers'""",
                          (key,))

                #Now apply the test
                for xxx in ctra2:
                    n_outliers=float(xxx[0])
                    if ( (abs(discrepmean) <= maxdev) and
                         (n_outliers < maxoutliers) ):
                        idlist.append(key)
                        print name, discrepmean, n_outliers
                        #If it passes the test, update the attention flag
                        db.execute("""UPDATE result_scalar SET attn = 'N'
                                      WHERE key_id = ?""",(key,))
                        #and insert the reason
                        db.execute("""INSERT INTO result_tra
                               ( key_id, name, value ) values (?, ?, ? )""" ,
                   ( key, "attn_code", "autoaccept") )


    db.commit()
    db.close()
    print len(idlist), " acceptable failures found and marked"

    #Make a qid so we can find these later if we want to
    if len(idlist) > 0:
        qdb = sqlite3.connect("/aten/data1/ssb/test/stf/cgi/db/stf_query.db")
        
        # create a new qid
        now = time.time()
        c = qdb.execute("INSERT INTO query_id ( time ) VALUES ( ? ) ",(now,))
        qid = c.lastrowid
        qdb.commit()

        #Now make our list
        for k in idlist:
            qdb.execute("INSERT INTO query ( qid, key_id ) VALUES ( ?, ? ) ", (qid, k) )
            #print "Insert loop: ", k, time.asctime()

        qdb.commit()
        qdb.close()

        #Write a URL
        url="http://stsdas.stsci.edu/cgi-bin/stf.cgi?query=summary&qid=%s\n"%qid
        sys.stdout.write(url)

if __name__ == '__main__':
    run(*sys.argv[1:])
