_,*a=open(0)
for i in a:
    s=0
    j,*b=map(int,i.split())
    for k,p in enumerate(b):
        for q in b[:k]:
            if q>p:s+=1
    print(j,s)