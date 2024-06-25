a=open(0)
t=[]
for _ in range(int(next(a))):
    n=int(next(a))
    m=0
    for r in sorted(map(int,next(a).split())):
        if m<n*r:m=n*r
        n-=1
    t.append(m)
print(*t,sep='\n')