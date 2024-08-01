def main():
    N,M=map(int,open(0).read().split())
    t=0
    while True:
        if N==1:
            return t,M+t-1
        if M==1:
            return N+t-1,t
        if N==2 or M==2:
            return t,t+1
        N-=2
        M-=2
        t+=1
print(*main())