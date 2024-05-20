def main():
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
    r=t=10**9
    for h in b:
        s,e=0,n
        while s<e:
            m=(s+e+1)//2
            if h>c[m-1]:s=m
            else:e=m-1
        if t-1>e:r=e
        elif t>1:r=t-1
        else:r=0
        q.append(r)
        if t>r:t=r
    print(" ".join(map(str, q)))
main()