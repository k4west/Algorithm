def dfs(i):
    if v[i]:return
    v[i]=True
    for j in g[i]:
        t[j]='1'
        dfs(j)
n,*a=open(0)
N,M=map(int,n.split())
v=[False]*(N+1)
t=['0']*(N+1)
g=[set() for i in range(N+1)]
for i in a:
    x,y=map(int,i.split())
    g[y].add(x)
if g[1]:dfs(1)
else: t[1]='1'
print(''.join(t[1:]))