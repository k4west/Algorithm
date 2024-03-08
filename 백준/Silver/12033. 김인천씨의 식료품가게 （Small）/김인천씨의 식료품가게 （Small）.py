import sys
input = sys.stdin.readline
for i in range(int(input())):
    discounted = []
    n = int(input())
    prices = list(map(int, input().split()))
    for j in range(n):
        if (org := prices[j] * 4 // 3) in prices:
            discounted.append(prices[j])
            prices.remove(org)
    print(f"Case #{i+1}: {' '.join(map(str, discounted))}")