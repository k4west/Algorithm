import sys


def pooling(board, n):
    new = []
    for i in range(n):
        a, b = 2 * i, 2 * i + 1
        tmp = []
        for j in range(n):
            t = sorted(board[a][2 * j : 2 * (j + 1)] + board[b][2 * j : 2 * (j + 1)])[2] 
            tmp.append(t)
        new.append(tmp)
    return new


input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

while n > 1:
    n //= 2
    board = pooling(board, n)
print(board[0][0])