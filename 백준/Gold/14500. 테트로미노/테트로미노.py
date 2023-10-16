from sys import stdin
input = stdin.readline
ans = 0

def main():
    N, M = map(int, input().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[False] * M for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    m = max((max(li) for li in T))
    
    def dfs(y, x, cnt, s):
        global ans
        if cnt == 4:
            ans = max(ans, s)
            return
        if ans > s + m*(4-cnt):
            return
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if cnt == 2:
                    visited[ny][nx] = True
                    dfs(y, x, cnt+1, s+T[ny][nx])
                    visited[ny][nx] = False
                visited[ny][nx] = True
                dfs(ny, nx, cnt+1, s+T[ny][nx])
                visited[ny][nx] = False

    for row in range(N):
        for col in range(M):
            visited[row][col] = True
            dfs(row, col, 1, T[row][col])
            visited[row][col] = False

    print(ans)


if __name__ == "__main__":
    main()
