a=open(0)
f=lambda:map(int,next(a).split())
d=((0,1),(1,0),(0,-1),(-1,0))
n,m=f()
g=[[*f()] for _ in range(n)]
h=[]
for r in range(n-1):
    i,j,c=r,0,0
    v={(i,j,c)}
    while 0<=i<n and 0<=j<m:
        k,e=g[i][j],d[c]
        i+=k*e[0]
        j+=k*e[1]
        if (t:=(i,j,c)) in v:h.append(r+1);break
        else:v.add(t)
        c=(c+1)%4
print(len(h))
if h:print(*h)