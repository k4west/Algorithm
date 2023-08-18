import sys
input = sys.stdin.readline
A = [list(map(int, input().split())) for _ in range(5)]
B = [list(map(int, input().split())) for _ in range(5)]
bingo = 0

def f(A, i, j):
    count = 0
    if i == j and A[0][0] + A[1][1] + A[2][2] + A[3][3]+ A[4][4] == 0:
        count += 1
    if i + j == 4 and A[0][4] + A[1][3] + A[2][2] + A[3][1]+ A[4][0] == 0:
        count += 1
    if sum(A[i]) == 0:
        count += 1
    if A[0][j] + A[1][j] + A[2][j] + A[3][j]+ A[4][j] == 0:
        count += 1
    return count

for r in range(5):
    for c in range(5):
        n = B[r][c]
        for i in range(5):
            if n in A[i]:
                for j in range(5):
                    if A[i][j] == n:
                        A[i][j] = 0
                        break
                bingo += f(A, i, j)
                if bingo >= 3:
                    print(r * 5 + c + 1)
                    exit()