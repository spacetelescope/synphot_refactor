def run():
    bzfile=open('bzspectype.ascii')
    bz={}
    for line in bzfile:
        name,type=line.strip().split()
        bz[type]=name
    bzfile.close()

    pfile=open('pickles_spectype.txt')
    pickles={}
    for line in pfile:
        try:
            name,type,temp=line.strip().split()
            pickles[type]=name
        except ValueError:
            pass
    pfile.close()

    return bz,pickles
      
def replace(bz,pickles):
    out=open('replace.txt','w')
    nomatch=[]
    for k in bz:
        try:
            newmod=pickles[k]
        except KeyError:
            newmod=pickles[subs[k.strip()].strip()]
        cmd="sed -i 's/%s/%s/' $x\n"%(bz[k].lower(),newmod)
        out.write(cmd)
    out.close()
    return nomatch

def gencand(nomatch,pickles):
    out=open('candidates.txt','w')
    for k in nomatch:
        cand=[]
        for j in pickles:
            if j[0]==k[0]: cand.append(j)
        cand.sort()
        out.write("%s: %s\n"%(k,cand))
    out.close()

subs = { 'A1V': 'A2V',
         'A2I': 'A0I     ',
         'A2III': 'A0III',
         'A3III': 'A0III',
         'A7III': 'A5III',
         'A7V': 'A5V',
         
         'B0.5I': 'B0I',
         'B0.5III': 'B1-2III',
         'B1III': 'B1-2III',
         'B2III': 'B1-2III',
         'B2V': 'B3V',
         'B5V': 'B5-7V',
         'B7III': 'B5III',
         'B7V':  'B5-7V', 
         'B8III': 'B9III',
         'B9.5III': 'B9III',
         'B9V': 'B8V', 
         
         'F2I':  'F2II', 
         'F6V':  'F5V', 
         'F7V': 'F8V',
         
         'G1V':  'G2V',
         'G2I':  'G0I',
         'G9III':  'G8III',

         'K2III': 'K3III', 
         'K3V': 'K2V', 
         'K6III': 'K5III', 
         'K9V': 'K7V',
         
         'M1III': 'M0III', 
         'M1M2I':'M2I',
         'M1V': 'M2V', 
         'M3III':  'M5III',
         'M4III':  'M5III',
         'M6III':  'M5III',
         'M6V': 'M5V',
         
         'O7I': 'O8III', 
         'O7V': 'O5V', 
         'O8V': 'O9V',
         'O9.5I':  'O9V',
         'O9III': 'O8III'}
