import sys

input = sys.stdin.readline
x, y = map(int, input().split())
yy = 0
for _ in range(int(input())):
    l, u, f = map(float, input().split())
    y -= (dist := u - l)
    yy += dist * f
print(f"{x / (y + yy):0.6f}")