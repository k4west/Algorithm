N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
B = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    print(*[A[i][j] + B[i][j] for j in range(M)])