import sys
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(9)]
# arr = [list(input().rstrip().split()) for _ in range(9)]

def check(r, c, n):
    for i in range(9):
        if n == arr[r][i]:
            return False
    for j in range(9):
        if n == arr[j][c]:
            return False
    r, c = r//3*3, c//3*3
    for i in range(3):
        for j in range(3):
            if n == arr[r+i][c+j]:
                return False
    return True

def bt(s):
    for i in range(s, 9):
        for j in range(9):
            if arr[i][j] != '0':
                continue
            for k in map(str, range(1, 10)):
                if not check(i, j, k):
                    continue
                arr[i][j] = k
                bt(i)
                arr[i][j] = '0'
            return
    for row in arr:
        print(*row, sep="")
    sys.exit()

bt(0)