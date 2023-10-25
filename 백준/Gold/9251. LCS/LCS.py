import sys
input = sys.stdin.readline

def main():
    s1 = input().rstrip()
    s2 = input().rstrip()
    n1, n2 = len(s1) + 1, len(s2) + 1

    dp = [[0]*(n1) for _ in range(n2)]

    for i in range(1, n2):
        s = s2[i-1]
        for j in range(1, n1):
            if s == s1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[n2-1][n1-1])

if __name__ == "__main__":
    main()