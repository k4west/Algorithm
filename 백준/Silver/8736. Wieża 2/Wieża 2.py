def bi(E,h):
    s,e=0,E
    while s<e:
        m=(s+e+1)//2
        if h>c[m-1]:s=m
        else:e=m-1
    return e
u=open(0)
f=lambda:map(int,next(u).split())
n,m=f()
a=f()
b=f()
q=[]
p=next(a)
c=[p]
for i in a:
    if p<i:p=i
    c.append(p)
r=s=10**9
for h in b:
    if s-1>(t:=bi(n,h)):r=t
    elif s>1:r=s-1
    else:r=0
    q.append(r)
    if s>r:s=r
print(*q)