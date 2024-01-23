import sys

sys.setrecursionlimit(10**6)


def main():
    input = sys.stdin.readline
    d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    N, M = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    v = [[0] * (M) for _ in range(N)]
    safe_zone = k = 0

    def dfs(r, c, k):
        dr, dc = d[graph[r][c]]
        if not v[nr := r + dr][nc := c + dc]:
            v[nr][nc] = k
            return dfs(nr, nc, k)
        else:
            if v[nr][nc] == k:
                return 1
            return 0

    for i in range(N):
        for j in range(M):
            if not v[i][j]:
                k += 1
                v[i][j] = k
                safe_zone += dfs(i, j, k)

    print(safe_zone)


if __name__ == "__main__":
    main()
