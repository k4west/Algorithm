import sys
from collections import deque

def main():
    M, N, H = map(int, sys.stdin.readline().split())
    tomato = [[] for _ in range(H)]
    ripen = deque()
    new_ripen = deque()
    d = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
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
        for dm, dn, dh in d:
            nh, nn, nm = h + dh, n + dn, m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if not tomato[nh][nn][nm]:
                    new_ripen.append((nh, nn, nm))
                    tomato[nh][nn][nm] = 1
    
    for i in range(H):
        for col in range(N):
            if 0 in tomato[i][col]:
                    print('-1')
                    return        
    print(days)

if __name__ == "__main__":
    main()