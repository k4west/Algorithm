a = open(0)
N, M = map(int, next(a).split())
C = list(map(int, a.read().split()))

temp, result = 0, 0
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            temp = C[a] + C[b] + C[c]
            if result < temp <= M:
                result = temp

print(result)