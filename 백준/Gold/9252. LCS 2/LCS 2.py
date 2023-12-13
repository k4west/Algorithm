import sys
input = sys.stdin.readline

def main():
    s1 = input().rstrip()
    s2 = input().rstrip()

    dp = [""] * max(len(s1), len(s2))

    for a in s1:
        c, s = 0, ""
        for i, b in enumerate(s2):
            if c < (t:=len(dp[i])):
                c = t
                s = dp[i]
            elif a == b:
                dp[i] = s + b

    ans = ""
    for s in dp:
        if len(s) > len(ans):
            ans = s
    print(len(ans))
    if ans: print(ans)

if __name__ == "__main__":
    main()