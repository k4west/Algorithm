def main():
    a=open(0)
    N,K=map(int,next(a).split())
    d=[*map(int,next(a).split())]
    s=sum(d)
    q,r=divmod(K,s)
    q%=2
    if q:d=d[::-1]
    for i,j in enumerate(d):
        if r>=j:r-=j
        else:break
    print([i+1,N-i][q])
main()