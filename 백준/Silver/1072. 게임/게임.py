import sys
X,Y=map(int, sys.stdin.readline().split())
if(Z:=(Y*100)//X)>=99:print(-1)
else:
    l,r=1,1000000000
    while l<=r:
        m=(l+r)//2
        if(Y+m)*100//(X+m)>Z:r=m-1
        else:l=m+1
    print(l)