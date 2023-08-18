import sys
input = sys.stdin.readline
N = int(input())
p = [0] * N

for n in range(N):
    p[n] = list(map(int, input().split()))
p.sort()

for q in p:
    print(' '.join(map(str, q)))