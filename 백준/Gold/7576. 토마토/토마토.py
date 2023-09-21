import sys
def f():
    M, N = map(int, sys.stdin.readline().split())
    A =  [[] for _ in range(N)]
    T = []
    for i in range(N):
        A[i] = list(map(int, sys.stdin.readline().split()))
        for j, t in enumerate(A[i]):
            if t==1:
                T.append((i,j))
    c = -1
    while T:
        c += 1
        temp = []
        for t in T:
            i, j = t
            if i > 0 and not A[i-1][j]:
                A[i-1][j] = True
                temp.append((i-1,j))
            if i < N-1 and not A[i+1][j]:
                A[i+1][j] = True
                temp.append((i+1,j))
            if j > 0 and not A[i][j-1]:
                A[i][j-1] = True
                temp.append((i,j-1))
            if j < M-1 and not A[i][j+1]:
                A[i][j+1] = True
                temp.append((i,j+1))
        T = temp
    for a in A:
        if 0 in a:
            print(-1)
            return
    print(c)
if  __name__ == "__main__":
    f()