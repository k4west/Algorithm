import sys
def f(s, A, N, M):
    v = [[False] * M for _ in range(N)]
    v[s[0]][s[1]] = True
    q = [s]
    c = 0
    while q:
        i, j = q.pop(0)
        if A[i][j] == 'P':
            c += 1
        if j<M-1 and A[i][j+1] != 'X' and not v[i][j+1]:
            v[i][j+1] = True
            q.append((i, j+1))
        if j>0 and A[i][j-1] != 'X' and not v[i][j-1]:
            v[i][j-1] = True
            q.append((i, j-1))
        if i<N-1 and A[i+1][j] != 'X' and not v[i+1][j]:
            v[i+1][j] = True
            q.append((i+1, j))
        if i>0 and A[i-1][j] != 'X' and not v[i-1][j]:
            v[i-1][j] = True
            q.append((i-1, j))
    return c
def m():
    N, M = map(int, sys.stdin.readline().split())
    A = []
    for i in range(N):
        li = list(sys.stdin.readline().rstrip())
        A.append(li)
        if 'I' in li:
            for j, a in enumerate(li):
                if a =='I':
                    s = (i, j)
    n = f(s, A, N, M)
    print(n if n else 'TT')
if __name__=="__main__":
    m()