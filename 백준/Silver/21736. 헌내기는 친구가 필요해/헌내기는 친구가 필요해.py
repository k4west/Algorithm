import sys
from collections import deque
def f(x, y, A, N, M):
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    v = [[False] * M for _ in range(N)]
    v[x][y] = True
    c = 0
    queue = deque([(x, y)])
    while queue:
        i, j = queue.popleft()
        for dx, dy in d:
            ni, nj = i + dx, j + dy
            if 0 > ni or ni >= N or 0 > nj or nj >= M: continue
            if v[ni][nj]: continue
            if A[ni][nj] == 'X': continue
            if A[ni][nj] == 'P': c += 1
            v[ni][nj] = True
            queue.append((ni, nj))
    if c: print(c)
    else: print('TT')

def m():
    N, M = map(int, sys.stdin.readline().split())
    A = []
    for i in range(N):
        li = list(sys.stdin.readline().rstrip())
        A.append(li)
        if 'I' in li:
            x, y = (i, li.index('I'))
    f(x, y, A, N, M)
    
if __name__ == "__main__":
    m()