import sys

def main():
    N = int(sys.stdin.readline())
    ALL = 2 ** 10 - 1
    mod = 1_000_000_000
    cnt = 0
    dp = [[[0] * (ALL + 1) for _ in range(10)] for _ in range(N+1)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for i in range(2, N+1):
        for j in range(10):
            for k in range(ALL + 1):
                if not j:
                    dp[i][0][k | (1 << 0)] = (dp[i][0][k | (1 << 0)] + dp[i - 1][1][k]) % mod
                elif j == 9:
                    dp[i][9][k | (1 << 9)] = (dp[i][9][k | (1 << 9)] + dp[i - 1][8][k]) % mod
                else:
                    dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k]) % mod

    for i in range(10):
        cnt += dp[N][i][ALL]
        cnt %= mod
    print(cnt)

if __name__ == "__main__":
    main()