a=open(0)
r,c=map(int,next(a).split())
m=[[*map(int,next(a).split())] for _ in range(r)]
for _ in range(int(next(a))):
    q,k,v=next(a).split()
    k,v=map(int,(k,v))
    if q=='row':
        for i in range(c):m[k-1][i] += v
    else:
        for i in range(r):m[i][k-1] += v
m=sum(m,[])
print(sum(m), min(m), max(m))