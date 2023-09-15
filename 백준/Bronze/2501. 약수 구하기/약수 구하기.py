from sys import stdin
N, K = map(int, stdin.readline().split())
i = 0
for _ in range(K):
    if i == N:
        i = 0
        break
    i += 1
    while N%i:
        i += 1
print(i)