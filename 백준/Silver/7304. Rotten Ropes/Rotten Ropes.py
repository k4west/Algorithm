for _ in range(int(input())):
    n=int(input());m=0
    for r in sorted(map(int,input().split())):
        if m<n*r:m=n*r
        n-=1
    print(m)