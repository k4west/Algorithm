import sys

input = sys.stdin.readline
n = int(input())
grid = [input().rstrip() for _ in range(n)]
ans = 1


def more_than_3(line):
    b = w = 0
    for s in line:
        if s == "B":
            w = 0
            b += 1
            if b == 3:
                return True
        if s == "W":
            b = 0
            w += 1
            if w == 3:
                return True
    return False


for row in grid:
    if row.count("W") != n // 2:
        ans = 0
        break
    if more_than_3(row):
        ans = 0
        break

if ans:
    for col in zip(*grid):
        if col.count("W") != n // 2:
            ans = 0
        if more_than_3(col):
            ans = 0
            break
print(ans)