d={'U':(0,-1,1),'D':(0,1,1),'L':(-1,0,2),'R':(1,0,2)}
N,a=open(0)
N=int(N)
a=a.strip()
G=[[0]*N+[-1] for _ in range(N)]
x=y=0
for i in a:
    dx,dy,t=d[i]
    if 0<=(nx:=x+dx)<N and 0<=(ny:=y+dy)<N:
        G[y][x]|=t
        G[ny][nx]|=t
        x,y=nx,ny
print(''.join('.|-+\n'[g] for g in sum(G,[])))