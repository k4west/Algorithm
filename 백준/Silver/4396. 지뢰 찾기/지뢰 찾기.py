import sys
input = sys.stdin.readline

n = int(input())
d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
board = [list(input().rstrip()) for _ in range(2*n)]
flag = False
for i in range(n):
    for j in range(n):
        if board[i+n][j] == 'x':
            if board[i][j] == '*':
                flag = True
            cnt = 0
            for di, dj in d:
                if 0<=(ni:=i+di)<n and 0<=(nj:=j+dj)<n and board[ni][nj]=='*':
                    cnt += 1
            board[i+n][j] = str(cnt)
if flag:
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                board[i+n][j] = '*'
for line in board[n:]:
    print("".join(line))