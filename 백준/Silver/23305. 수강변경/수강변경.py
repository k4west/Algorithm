def main():
    n,*a=map(int,open(0).read().split())
    d=[0]*(10**6+1)
    for i in a[:n]:
        d[i]+=1
    for i in a[n:]:
        if d[i]:
            d[i]-=1
    print(sum(d))
main()