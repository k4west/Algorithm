import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    consultings = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0] * (N + 1)

    for i in range(N):
        t, p = consultings[i]
        for j in range(i + t, N + 1):
            if dp[j] < (np := dp[i] + p):
                dp[j] = np

    print(dp[-1])


if __name__ == "__main__":
    main()