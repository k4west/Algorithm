N, M = map(int, input().split())
arr = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i:j+1] = arr[j:i-1:-1]
print(*arr[1:])