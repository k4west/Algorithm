import sys

def pooling(board, n):
    new = []
    for i in range(n):
        tmp = []
        for j in range(n):
            x, y = i*2, j*2
            t = [board[x][y], board[x][y+1], board[x+1][y], board[x+1][y+1]]
            t.sort()
            tmp.append(t[2])
        new.append(tmp)
    return new

input = sys.stdin.readline
n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

while n > 1:
    n //= 2
    board = pooling(board, n)
print(board[0][0])