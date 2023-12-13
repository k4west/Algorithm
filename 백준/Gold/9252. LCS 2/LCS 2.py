import sys
input = sys.stdin.readline

def main():
    s1 = input().rstrip()
    s2 = input().rstrip()

    dp = [[0, ""] for _ in range(1000)]

    for a in s1:
        c, s = 0, ""
        for i, b in enumerate(s2):
            if c < dp[i][0]:
                c = dp[i][0]
                s = dp[i][1]
            elif a == b:
                dp[i][0] = c + 1
                dp[i][1] = s + b

    c, s = max(dp)
    print(c)
    if s: print(s)
    
if __name__ == "__main__":
    main()