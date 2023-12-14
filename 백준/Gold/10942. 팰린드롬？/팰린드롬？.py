import sys
input = sys.stdin.readline

def main():
    N = int(input())
    num = list(map(int, input().split()))
    M = int(input())
    dp = [['0']*N for _ in range(N)]
    ans = []
    
    for i in range(N):
        for s in range(N-i):
            e = s + i
            if s == e:
                dp[s][e] = '1'
            elif num[s] == num[e]:
                if s+1 == e:
                    dp[s][e] = '1'
                elif dp[s+1][e-1] == '1':
                    dp[s][e] = '1'
    
    for _ in range(M):
        S, E = map(int, input().split())
        ans.append(dp[S-1][E-1])
    print("\n".join(ans))

if __name__ == "__main__":
    main()