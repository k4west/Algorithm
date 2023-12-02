import sys
input = sys.stdin.readline

N = int(input())
area = 0
x, y = map(int, input().split())
x0, y0 = x, y
for i in range(N-1):
    x1, y1 = map(int, input().split())
    area += x0*y1 - x1*y0
    x0, y0 = x1, y1
area += x1*y - x*y1
ans = round(area/2, 1)
print(max(ans, -ans))