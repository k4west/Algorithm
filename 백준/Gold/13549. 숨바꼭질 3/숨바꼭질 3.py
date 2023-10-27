from sys import stdin
input = stdin.readline

def dfs(N, K):
    if N >= K:  return N-K
    if not N: return 1 + dfs(1, K)
    if not K%2: return min(K-N, dfs(N, K//2))
    return 1 + min(dfs(N, K-1), dfs(N, K+1))

def main():
    N, K = map(int, input().split())
    print(dfs(N,K))

if __name__ == "__main__":
    main()