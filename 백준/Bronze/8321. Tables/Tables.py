import sys
input = sys.stdin.readline
n, k, s = map(int, input().split())
ss = list(map(int, input().split()))
ss.sort()
rs = k * s
ns = 0
for idx, s in enumerate(ss[::-1], 1):
    ns += s
    if ns >= rs: break
print(idx)