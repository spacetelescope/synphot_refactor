import re
def run(inname):
    f=open(inname)
    f2=open(inname.replace('.txt','_key.txt'),'w')
    d={}
    dshort={}
    lookup={}
    namepat=re.compile('(acs[^ ]*fits)')
    compat = re.compile('"(.*)"')
    space = re.compile(r'\s+')
    count=0
    for nextline in f:
        line=space.sub(' ',nextline)
        x=re.search(namepat,line)
        fname=x.group(1)
        x=re.search(compat,line)
        comment=x.group(1)
        try:
            d[comment.strip()].append(fname)
        except KeyError:
            d[comment.strip()]=[fname]
            count+=1
            dshort[count]=comment.strip()
            lookup[comment.strip()]=count
        f2.write("%s     %d\n"%(fname,lookup[comment.strip()]))
    f.close()
    f2.close()
    out=open(inname.replace('.txt','_code.txt'),'w')
    for k in dshort:
        out.write('%s\t%s\n'%(k,dshort[k]))
    out.close()
                  
    return d,dshort
