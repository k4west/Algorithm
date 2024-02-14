import sys
input = sys.stdin.readline
n = int(input())
grid = [input().rstrip() for _ in range(n)]
ans = 1
def more_than_3(line):
    count = 0
    prev = "W"
    for s in line:
        if s == prev:
            count += 1
            if count == 3:
                return True
        else:
            count = 1
            prev = s
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
            break
        if more_than_3(col):
            ans = 0
            break
print(ans)
