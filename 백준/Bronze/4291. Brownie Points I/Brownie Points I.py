import sys

input = sys.stdin.readline
ans = []
while n := int(input()):
    li = [[*map(int, input().split())] for _ in range(n)]
    x0, y0 = li[n // 2]
    stan, ollie = 0, 0
    for x, y in li:
        if x == x0 or y == y0:
            continue
        if (x > x0 and y > y0) or (x < x0 and y < y0):
            stan += 1
        else:
            ollie += 1
    ans.append(f"{stan} {ollie}")
print("\n".join(ans))
