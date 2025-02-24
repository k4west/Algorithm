N, M = map(int, open(0).read().split())
t = s = 1
for i in range(N, M):
    t *= i
for i in range(2, M-N+1):
    s *= i
print(t//s)