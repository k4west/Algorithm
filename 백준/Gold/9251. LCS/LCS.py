import sys
input = sys.stdin.readline

def main():
    s1 = input().rstrip()
    s2 = input().rstrip()

    dp = [0] * 1000

    for a in s1:
        c = 0
        for i, b in enumerate(s2):
            if c < dp[i]:
                c = dp[i]
            elif b == a:
                dp[i] = c + 1

    print(max(dp))

if __name__ == "__main__":
    main()