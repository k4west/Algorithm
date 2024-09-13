def gcd(a,b):
    while b:a,b=b,a%b
    return a
def main():
    M,N=map(int,input().split());v=set()
    for i in range(M,N):
        for j in range(i+1,N+1):v.add((i//(k:=gcd(j,i)),j//k))
    print(2*len(v)+1)
main()