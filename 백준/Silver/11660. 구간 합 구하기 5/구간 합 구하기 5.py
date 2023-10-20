import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    li = [[0]*(N+1)]
    ans = []
    for _ in range(N):
        li.append([0] + list(map(int, input().split())))
    for i in range(1, N+1):
        for j in range(1, N+1):
            li[i][j] += li[i][j-1] + li[i-1][j] - li[i-1][j-1]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        ans.append(li[x2][y2] - li[x2][y1-1] - li[x1-1][y2] + li[x1-1][y1-1])
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()