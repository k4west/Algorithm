import sys
from collections import deque

def main():
    M, N, H = map(int, sys.stdin.readline().split())
    tomato = [[] for _ in range(H)]
    ripen = deque()
    d = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
    days = 1

    for i in range(H):
        for col in range(N):
            tomato[i].append(list(map(int, sys.stdin.readline().split())))
            for row in range(M):
                if tomato[i][col][row] == 1:
                    ripen.append((i, col, row))
    
    while ripen:
        h, n, m = ripen.popleft()
        c = tomato[h][n][m]
        for dm, dn, dh in d:
            nh, nn, nm = h + dh, n + dn, m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if not tomato[nh][nn][nm]:
                    ripen.append((nh, nn, nm))
                    tomato[nh][nn][nm] = c + 1
    
    for i in range(H):
        for col in range(N):
            for row in range(M):
                if tomato[i][col][row]:
                    days = max(days, tomato[i][col][row])
                else:
                    return -1
    return days - 1

if __name__ == "__main__":
    print(main())