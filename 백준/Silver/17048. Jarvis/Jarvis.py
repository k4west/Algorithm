N,A,B=open(0)
d={}
for a,b in zip(A.strip().split(),B.strip().split()):
    c=int(a)-int(b)
    if c in d:
        d[c]+=1
    else:
        d[c]=1
print(max(d.values()))