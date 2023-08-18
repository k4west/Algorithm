import sys
input = sys.stdin.readline

N = int(input())
l = [0] * N
for i in range(N):
    l[i] = list(map(str,input().split()))
    l[i][0] = int(l[i][0])

l = sorted(l, key = lambda x: x[0])

for x, y in l:
    print(x, y)