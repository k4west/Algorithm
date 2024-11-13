from collections import deque
def dfs(i):
    v[i] = 1
    q = deque([i])
    while q:
        i = q.popleft()
        for di in d:
            if b[(ni:=i+di)] > 0 and not v[ni]:
                v[ni] = 1
                q.append(ni)
        
n, m, *b = map(int, open(0).read().split())
d = (-1, 1, m, -m)
y = 0
while True:
    v = [0 for _ in range(n*m)]
    flag = False
    for i in range(1, n*m-1):
        if not v[i] and b[i] > 0:
            if flag:
                exit(print(y))
            dfs(i)
            flag = True
    if not flag:
        break
    for i in range(1, n*m-1):
        if b[i] > 0:
            b[i] -= sum([not v[i+di] for di in d])
    y += 1
print(0)