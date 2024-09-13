def gcd(a,b):
    while b:a,b=b,a%b
    return a
def main():
    M,N=map(int,input().split())
    v=[[False for _ in range(N+1)] for _ in range(N+1)]
    t=0
    for i in range(M,N):
        for j in range(i+1,N+1):
            if not v[i//(k:=gcd(j,i))][j//k]:v[i//k][j//k]=True;t+=1
    print(2*t+1)
main()