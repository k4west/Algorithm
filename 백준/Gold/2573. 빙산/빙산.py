from collections import deque
def dfs(r, c):
    v[m*r+c] = 1
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            if b[m*(nr:=r+dr)+(nc:=c+dc)] > 0 and not v[m*nr+nc]:
                v[m*nr+nc] = 1
                q.append((nr, nc))
        
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
n, m, *b = map(int, open(0).read().split())
y = 0
while True:
    v = [0]*(n*m)
    flag = False
    for r in range(1, n-1):
        for c in range(1, m-1):
            if not v[m*r+c] and b[m*r+c] > 0:
                if flag:
                    exit(print(y))
                dfs(r, c)
                flag = True
    if not flag:
        break
    for r in range(1, n-1):
        for c in range(1, m-1):
            if b[m*r+c] > 0:
                b[m*r+c] -= sum([not v[m*(r+dr)+c+dc] for dr, dc in d])
    y += 1
print(0)