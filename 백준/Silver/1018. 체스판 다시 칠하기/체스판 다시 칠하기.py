import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * M] * N
for i in range(N):
    board[i] = (list(map(str, input())))
    for j in range(M):
        board[i][j] = list(map(lambda x: 0 if x == 'B' else 1, board[i][j]))[0]

b = [(M - j) % 2 for j in range(M)]
w = [(M + 1 - j) % 2 for j in range(M)]

result = 32 

for n in range(N - 7):
    for m in range(M - 7):
        bc = 0 
        for s in range(n, n + 8):
            for t in range(m, m + 8):
                if s % 2 == 0:
                    bc += (board[s][t] - b[t]) ** 2
                if s % 2 == 1:
                    bc += (board[s][t] - w[t]) ** 2
        temp = min(bc, 64- bc) 
        result = min(result, temp) 

print(result)