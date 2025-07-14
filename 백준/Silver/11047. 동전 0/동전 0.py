N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
count = 0
for coin in coins[::-1]:
    if coin <= K:
        m = K//coin
        K -= coin * m
        count += m
print(count)