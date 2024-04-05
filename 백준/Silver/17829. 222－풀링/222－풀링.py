import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
while n > 1:
    n //= 2
    board = [[sorted(board[2 * i][2 * j : 2 * (j + 1)] + board[2 * i + 1][2 * j : 2 * (j + 1)])[2] for j in range(n)] for i in range(n)]
print(board[0][0])