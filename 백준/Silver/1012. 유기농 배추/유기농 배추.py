import sys
input = sys.stdin.readline
 
dy = [-1,1,0,0]
dx = [0,0,-1,1]
 
def mod(y,x):
    temp = [(y,x)]
    while temp:
        y ,x = temp.pop()
        for i in range(4):
            Y = y  + dy[i]
            X = x + dx[i]
            if 0 <= Y < N and 0 <= X < M and A[Y][X]:
                A[Y][X] = 0
                temp.append((Y,X))
 
for _ in range(int(input())):
    M,N,K = map(int,input().split())
    A = [[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        A[Y][X] = 1
    c = 0
    for a in range(N):
        for b in range(M):
            if A[a][b]:
                A[a][b] = 0
                c += 1
                mod(a,b)
                
    print(c)