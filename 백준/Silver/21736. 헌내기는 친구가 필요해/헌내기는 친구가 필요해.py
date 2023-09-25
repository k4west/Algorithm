import sys
sys.setrecursionlimit(10**6)
def f(i, j, A, v, N, M):
    c = 0
    if A[i][j] == 'P':
        c += 1
    if j<M-1 and A[i][j+1] != 'X' and not v[i][j+1]:
        v[i][j+1] = True
        c += f(i, j+1, A, v, N, M)
    if j>0 and A[i][j-1] != 'X' and not v[i][j-1]:
        v[i][j-1] = True
        c += f(i, j-1, A, v, N, M)
    if i<N-1 and A[i+1][j] != 'X' and not v[i+1][j]:
        v[i+1][j] = True
        c += f(i+1, j, A, v, N, M)
    if i>0 and A[i-1][j] != 'X' and not v[i-1][j]:
        v[i-1][j] = True
        c += f(i-1, j, A, v, N, M)
    return c
def m():
    N, M = map(int, sys.stdin.readline().split())
    A = []
    v = [[False] * M for _ in range(N)]
    for i in range(N):
        li = list(sys.stdin.readline().rstrip())
        A.append(li)
        if 'I' in li:
            x, y = (i, li.index('I'))
    v[x][y] = True
    n = f(x, y, A, v, N, M)
    print(n if n else 'TT')
if __name__=="__main__":
    m()