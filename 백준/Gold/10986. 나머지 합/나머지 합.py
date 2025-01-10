N, M = map(int, input().split())
arr = [*map(int, input().split())]+[0]
remain = [0 for _ in range(M)]
for i in range(N):
    arr[i] = (arr[i] + arr[i-1])%M
    remain[arr[i]] += 1
print(remain[0]*(remain[0]+1)//2 + sum(remain[i]*(remain[i]-1)//2 for i in range(1, M)))