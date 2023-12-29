import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    *memories, = map(int, input().split())
    *costs, = map(int, input().split())

    C = sum(costs)
    dp = [0]*(C+1)
    for i in range(N):
        m, c = memories[i], costs[i]
        for j in range(C, c-1, -1):
            dp[j] = min(M, max(dp[j], dp[j-c]+m))

    li = [c for c in range(C+1) if dp[c]==M]
    print(sorted(li)[0])

if __name__ == "__main__":
    main()