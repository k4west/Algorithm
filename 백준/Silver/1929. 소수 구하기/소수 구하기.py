import sys

def f(M,N):
    li = [False,False,True]+[i%2 for i in range(3,N+1)]
    for n in range(3, N+1, 2):
        if li[n]:
            li[n*n::n] = [False]*(N//n-n+1)
    return li[M:]

M, N = map(int, sys.stdin.readline().split())
li = f(M,N)
print("\n".join([str(n) for n, t in zip(range(M,N+1),li) if t]))