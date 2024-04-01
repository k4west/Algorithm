import sys
input = sys.stdin.readline
ans = []
while n := int(input()):
    li = [[*map(int, input().split())] for _ in range(n)]
    x0, y0 = li[n // 2]
    s = [0, 0]
    for x, y in li:
        t = (x - x0) * (y - y0)
        if t > 0: s[0] += 1
        elif t < 0: s[1] += 1
    ans.append(s)
print("\n".join(map(lambda x: " ".join(map(str, x)), ans)))