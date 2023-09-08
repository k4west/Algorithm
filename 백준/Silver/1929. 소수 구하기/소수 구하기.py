import sys

def f(N):
    li = [0,0,1]+[0 if i%2==0 else 1 for i in range(3,N+1)]
    for n in range(3, N+1, 2):
        if li[n]:
            li[n+n::n] = [0]*(N//n-1)
    return li

M, N = map(int, sys.stdin.readline().split())
li = f(N)
print("\n".join([str(n) for n, t in zip(range(M,N+1),li[M:]) if t]))