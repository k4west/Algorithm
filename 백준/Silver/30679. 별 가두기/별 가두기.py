def main():
    a=open(0);f=lambda:map(int,next(a).split());d=(0,1,0,-1);n,m=f();g=[[*f()] for _ in range(n)];h=[];v=[[[-1 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    for r in range(n-1):
        i,j,c=r,0,0
        while 0<=i<n and 0<=j<m and v[i][j][c]==-1:v[i][j][c]=r;k,p,q=g[i][j],d[c],d[(c+1)%4];i+=k*p;j+=k*q;c=(c+1)%4
        if 0<=i<n and 0<=j<m and (v[i][j][c]==r or v[i][j][c]+1 in h):h.append(r+1)
    print(len(h))
    if h:print(*h)
main()