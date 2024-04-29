import sys
input = sys.stdin.readline
n, m = map(int, input().split())
c = prev = 0
for d in map(int, input().split()):
    if prev > d:
        c += 1
    prev = d
print(c)