N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
B = [[*map(int, input().split())] for _ in range(N)]
print('\n'.join([' '.join(map(str, [A[i][j] + B[i][j] for j in range(M)])) for i in range(N)]))