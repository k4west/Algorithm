import sys
from collections import deque

def main():
    M, N, H = map(int, sys.stdin.readline().split())
    tomato = [[] for _ in range(H)]
    ripen = deque()
    new_ripen = deque()
    days = 0

    for i in range(H):
        box = []
        for j in range(N):
            row = list(map(int, sys.stdin.readline().split()))
            box.append(row)
            for k, t in enumerate(row):
                if t == 1:
                    ripen.append((i, j, k))
        tomato[i] = box
    
    while ripen or new_ripen:
        if not ripen:
            ripen, new_ripen = new_ripen, ripen
            days += 1

        h, n, m = ripen.popleft()
        h1, h2, n1, n2, m1, m2 = h + 1, h - 1, n + 1, n - 1, m + 1, m - 1
        if h1 < H and not tomato[h1][n][m]:
            new_ripen.append((h1, n, m))
            tomato[h1][n][m] = 1
        if 0 <= h2 and not tomato[h2][n][m]:
            new_ripen.append((h2, n, m))
            tomato[h2][n][m] = 1
        if n1 < N and not tomato[h][n1][m]:
            new_ripen.append((h, n1, m))
            tomato[h][n1][m] = 1
        if 0 <= n2 and not tomato[h][n2][m]:
            new_ripen.append((h, n2, m))
            tomato[h][n2][m] = 1
        if m1 < M and not tomato[h][n][m1]:
            new_ripen.append((h, n, m1))
            tomato[h][n][m1] = 1
        if 0 <= m2 and not tomato[h][n][m2]:
            new_ripen.append((h, n, m2))
            tomato[h][n][m2] = 1

    for i in range(H):
        for col in range(N):
            if 0 in tomato[i][col]:
                    print('-1')
                    return        
    print(days)

if __name__ == "__main__":
    main()