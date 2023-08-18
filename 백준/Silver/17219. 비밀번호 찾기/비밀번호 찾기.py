import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = {}
for _ in range(N):
    ad, pw = input().split()
    d[ad] = pw

for _ in range(M):
    print(d[input().strip()])