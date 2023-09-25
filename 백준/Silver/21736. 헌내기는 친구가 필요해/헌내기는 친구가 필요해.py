import sys
from collections import deque
def m():
    N, M = map(int, sys.stdin.readline().split())
    A = []
    v = [[False] * M for _ in range(N)]
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for i in range(N):
        li = list(sys.stdin.readline().rstrip())
        A.append(li)
        if 'I' in li:
            x, y = (i, li.index('I'))
    v[x][y] = True
    c = 0
    queue = deque([(x, y)])
    while queue:
        i, j = queue.popleft()
        if A[i][j] == 'P':
            c += 1
        for dx, dy in d:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M and A[ni][nj] != 'X' and not v[ni][nj]:
                v[ni][nj] = True
                queue.append((ni, nj))
    print(c if c else 'TT')
if __name__ == "__main__":
    m()