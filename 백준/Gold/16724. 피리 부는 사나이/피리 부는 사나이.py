import sys

sys.setrecursionlimit(10**6)


def main():
    input = sys.stdin.readline
    d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    N, M = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    v = set()
    safe_zone = 0

    def back(r, c):
        for dr, dc in d.values():
            if (
                0 <= (nr := r + dr) < N
                and 0 <= (nc := c + dc) < M
                and not (nr, nc) in v
            ):
                ddr, ddc = d[graph[nr][nc]]
                if r == nr + ddr and c == nc + ddc:
                    v.add((nr, nc))
                    back(nr, nc)

    def go(r, c):
        dr, dc = d[graph[r][c]]
        if (nr := r + dr, nc := c + dc) not in v:
            v.add((nr, nc))
            go(nr, nc)
        back(nr, nc)

    for i in range(N):
        for j in range(M):
            if (i, j) not in v:
                v.add((i, j))
                go(i, j)
                back(i, j)
                safe_zone += 1

    print(safe_zone)


if __name__ == "__main__":
    main()