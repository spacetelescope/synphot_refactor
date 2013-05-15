""" Use this script to remove the pinned versions from the allpinned
directory created by extrap.py."""

from extrap import fincre
import os, sys

def run(flist,dirname):
    f=open(flist)
    for fname in f:
        #increment the version number
        newname=fincre(fname.strip())
        #delete the file
        try:
            os.unlink(os.path.join(dirname,newname))
        except (OSError,IOError), e:
            print "Error removing %s"%newname
            print "...%s"%str(e)
    f.close()

if __name__ == '__main__':
    print ' '.join(sys.argv)
    run(*sys.argv[1:])
