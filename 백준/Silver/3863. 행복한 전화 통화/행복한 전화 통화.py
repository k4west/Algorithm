def main():
    a=open(0)
    t=[]
    while True:
        n,m=map(int,next(a).split())
        if n==0:
            break
        c=[[*map(int,next(a).split()[2:])] for _ in range(n)]
        d=[[*map(int,next(a).split())] for _ in range(m)]
        for i,j in d:
            s=0
            for p,q in c:
                if i<=p<i+j or p<=i<p+q:
                    s+=1
            t.append(s)
    print('\n'.join(map(str,t)))
main()