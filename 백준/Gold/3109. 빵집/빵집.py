from collections import deque
def dfs(r, c):
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        a[r][c] = ''
        t = []
        c += 1
        for dr in d:
            if 0 > (nr:=r+dr) or nr >= R or a[nr][c]!='.':
                continue
            if c == C-1:
                return True
            t.append((nr, c))
        q.extendleft(t)
    return False

d = (1, 0, -1)
a = open(0)
R, C = map(int, next(a).split())
a = [*map(list, a.read().split())]
print(sum(dfs(r, 0) for r in range(R)))