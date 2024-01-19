import sys

input = sys.stdin.readline

for _ in range(int(input())):
    h, m, s = map(int, input().split())
    C = s / 60
    B = m / 60 + C / 60
    A = h / 12 + B / 12
    li = sorted((A, B, C))
    print(360 * min(li[2] - li[1], li[1] - li[0], 1 + li[0] - li[2]))