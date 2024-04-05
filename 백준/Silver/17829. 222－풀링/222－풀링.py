import sys

def pooling(board, n):
    new = []
    for i in range(n):
        a, b = 2 * i, 2 * i + 1
        tmp = []
        for j in range(n):
            t = [board[a][2*j], board[a][2*j+1], board[b][2*j], board[b][2*j+1]]
            t.sort()
            tmp.append(t[2])
        new.append(tmp)
    return new

input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append([*map(int, input().split())])

while n > 1:
    n //= 2
    board = pooling(board, n)
print(board[0][0])