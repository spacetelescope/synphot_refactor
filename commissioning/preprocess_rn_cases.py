import sys

def main(fname):
    case = """class %sC%d(basecase.calcspecCase):
    def setUp(self):
        self.spectrum='%s'
        self.obsmode=None
        self.setglobal(__file__)
        self.runpy()\n\n"""
        
    instr=getinstr(fname)
    f=open(fname)
    out=open(fname.replace('.txt','.py'),'w')
    out.write("import basecase\n")
    count=0
    for line in f:
        if not line.startswith('#'):
            cmd=line.strip()
            if (len(cmd) != 0):
               count+=1            
               out.write(case%(instr,count,cmd))
    out.close()
    f.close()

def getinstr(fname):
    ilist=['acs','nicmos','stis','wfc3']
    _fname=fname.lower()
    for iname in ilist:
        if iname in _fname:
            return iname
    raise ValueError("Instrument not found in filename")
               
if __name__ == '__main__':
    main(sys.argv[1])
