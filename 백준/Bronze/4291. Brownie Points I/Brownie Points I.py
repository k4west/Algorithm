import sys

input = sys.stdin.readline
ans = []
while n := int(input()):
    li = [[*map(int, input().split())] for _ in range(n)]
    x0, y0 = li[n // 2]
    s = [0, 0]
    for x, y in li:
        if x == x0 or y == y0:
            continue
        if (x > x0 and y > y0) or (x < x0 and y < y0):
            s[0] += 1
        else:
            s[1] += 1
    ans.append(" ".join(map(str, s)))
print("\n".join(ans))
