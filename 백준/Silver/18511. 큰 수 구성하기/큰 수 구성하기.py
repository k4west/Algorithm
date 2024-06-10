from itertools import product
a=open(0)
N,_=next(a).split()
s=sorted(set(next(a).split()),reverse=True)
n=len(N)
r=''
if (m:=min(s))>N[0] or (m==N and m*(n-1)>N[1:]):r=max(s)*(n-1)
while not r:
    for i in product(s,repeat=n):
        if (t:=''.join(i))<=N:r=t;break
print(r)