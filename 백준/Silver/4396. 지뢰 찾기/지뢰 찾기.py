import sys
input = sys.stdin.readline

n = int(input())
d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

bombs = [input().rstrip() for _ in range(n)]
board = [list(input().rstrip()) for _ in range(n)]
flag = False
for i in range(n):
    for j in range(n):
        if board[i][j] == 'x':
            if bombs[i][j] == '*':
                flag = True
            cnt = 0
            for di, dj in d:
                if 0<=(ni:=i+di)<n and 0<=(nj:=j+dj)<n and bombs[ni][nj]=='*':
                    cnt += 1
            board[i][j] = str(cnt)
if flag:
    for i in range(n):
        for j in range(n):
            if bombs[i][j] == '*':
                board[i][j] = '*'
for line in board:
    print("".join(line))