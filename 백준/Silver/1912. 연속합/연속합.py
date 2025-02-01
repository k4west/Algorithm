def main():
    n, *arr = map(int, open(0).read().split())
    dp = [0 for _ in range(n+1)]
    
    for i in range(n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    dp[-1] = dp[0]
    print(max(dp))
main()