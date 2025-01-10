N, M, *arr = map(int, open(0).read().split())
remain = [0 for _ in range(M)]
s = 0
for a in arr:
    s = (s+a)%M
    remain[s] += 1
print(remain[0] + sum(remain[i]*(remain[i]-1)//2 for i in range(M)))