import sys

def f(N):
    li = ["","",True]+[i%2 for i in range(3,N+1)]
    for n in range(3, N+1, 2):
        if li[n]:
            li[n*n::n] = [""]*(N//n-n+1)
    return li

M, N = map(int, sys.stdin.readline().split())
li = f(N)
print("\n".join([str(n) for n, t in zip(range(M,N+1),li[M:]) if t]))