from sys import stdin
input = stdin.readline
ans = 0

def main():
    N, M = map(int, input().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    T = [list(map(int, input().split())) for _ in range(N)]
    m = max(map(max, T))
    
    def dfs(y, x, cnt, s):
        global ans
        if cnt == 4:
            ans = max(ans, s)
            return
        if ans > s + m*(4-cnt):
            return
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and T[ny][nx]:
                t = T[ny][nx]
                if cnt == 2:
                    T[ny][nx] = False
                    dfs(y, x, cnt+1, s+t)
                    T[ny][nx] = t
                T[ny][nx] = False
                dfs(ny, nx, cnt+1, s+t)
                T[ny][nx] = t

    for row in range(N):
        for col in range(M):
            t = T[row][col]
            T[row][col] = False
            dfs(row, col, 1, t)
            T[row][col] = t

    print(ans)


if __name__ == "__main__":
    main()
