import sys
input = sys.stdin.readline

M, N = map(int, input().split())
A =  [[False]*M for _ in range(N)]
T = []
c, e = -1, 0
for i in range(N):
    for j, t in enumerate(input().split()):
        if t=='1':
            T.append((i,j))
            A[i][j] = True
        elif t=='-1':
            A[i][j] = -1
            e += 1

def f(A, t):
    tmp = []
    i, j = t
    if i > 0 and not A[i-1][j]:
        A[i-1][j] = True
        tmp.append((i-1,j))
    if i < N-1 and not A[i+1][j]:
        A[i+1][j] = True
        tmp.append((i+1,j))
    if j > 0 and not A[i][j-1]:
        A[i][j-1] = True
        tmp.append((i,j-1))
    if j < M-1 and not A[i][j+1]:
        A[i][j+1] = True
        tmp.append((i,j+1))
    return tmp
    
def g(A, T):
    temp = []
    for t in T:
        temp.extend(f(A, t))
    return temp

while T:
    c += 1
    T = g(A, T)

if N*M == sum(sum(A, [])) + 2*e: print(c)
else: print(-1)