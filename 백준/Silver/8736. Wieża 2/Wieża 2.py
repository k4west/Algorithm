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
        q.append(r:=max(0,min(t-1,e)))
        if t>r:t=r
    print(" ".join(map(str, q)))
main()