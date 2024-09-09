def main():
    n,*a=open(0)
    N,M=map(int,n.split())
    g=[set() for i in range(N+1)]
    for i in a:
        x,y=map(int,i.split())
        g[y].add(x)
    v=[False]*(N+1)
    t=['0']*(N+1)
    o=g[1].copy()
    while o:
        oo=set()
        for i in o:
            if not v[i]:
                v[i]=True
                n=g[i]-g[1]
                g[1]|=n
                oo|=n
        o,oo=oo,set()
    for i in g[1]:t[i]='1'
    if not g[1]:t[1]='1'
    print(''.join(map(str,t[1:])))
main()