import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    dp = [0]*(K+1)
    for i in range(1, N+1):
        tmp = dp.copy()
        W, V = map(int, input().split())
        for j in range(W, K+1):
            dp[j] = max(tmp[j], tmp[j-W]+V)

    print(dp[K])
    
if __name__ == "__main__":
    main()