import sys

input = sys.stdin.readline
N, L = map(int, input().split())
cnt = e = 0
for i in sorted(map(int, input().split())):
    if i <= e: continue
    cnt += 1
    e = i + L - 1
print(cnt)