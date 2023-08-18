import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n = list(range(1, N + 1))
result = []
k = 0
for i in range(N):
    k += K - 1
    k %= (N - i)
    result.append(str(n.pop(k)))

print('<', ', '.join(result), '>', sep = '')