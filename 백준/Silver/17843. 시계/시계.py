import sys

input = sys.stdin.readline
for _ in range(int(input())):
    h, m, s = map(int, input().split())
    li = sorted((h / 12 + m / 720 + s / 43200, m / 60 + s / 3600, s / 60))
    print(360 * min(li[2] - li[1], li[1] - li[0], 1 + li[0] - li[2]))