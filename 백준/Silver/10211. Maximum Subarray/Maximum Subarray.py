def main():
    a = open(0)
    t = []
    for _ in range(int(next(a))):
        n = int(next(a))
        *arr, = map(int, next(a).split())
        dp = [0] * n
        dp[0] = arr[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+arr[i], arr[i])
        t.append(max(dp))
    print('\n'.join(map(str, t)))

main()