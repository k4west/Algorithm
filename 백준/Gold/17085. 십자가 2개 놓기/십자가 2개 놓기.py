def check(r0, c0, n0, r1, c1, n1):
    if r0 == r1:
        if c0 > c1:
            r0, c0, n0, r1, c1, n1 = r1, c1, n1, r0, c0, n0
        return c0+n0 < c1-n1
    elif c0 == c1:
        if r0 > r1:
            r0, c0, n0, r1, c1, n1 = r1, c1, n1, r0, c0, n0
        return r0+n0 < r1-n1
    if c0 > c1:
        r0, c0, n0, r1, c1, n1 = r1, c1, n1, r0, c0, n0
    if r0 < r1 and ((c0+n0 >= c1 and r0 >= r1-n1) or (r0+n0 >= r1 and c0 >= c1-n1)):
        return False
    if r0 > r1 and ((c0+n0 >= c1 and r0 <= r1+n1) or (r0-n0 <= r1 and c0 >= c1-n1)):
        return False
    return True

d = ((-1, 0), (1, 0), (0, -1), (0, 1))
a = open(0)
N, M = map(int, next(a).split())
board = [i.strip() for i in a.read().split()]
candi = [[] for _ in range(8)]
m = size = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '#':
            n = 0
            flag = True
            candi[n].append((i, j))
            while flag:
                n += 1
                for di, dj in d:
                    ni = i+n*di
                    nj = j+n*dj
                    if not (0<=ni<N) or not (0<=nj<M) or board[i+n*di][j+n*dj]=='.':
                        flag = False
                        break
                else:
                    candi[n].append((i, j))
                    if m < n:
                        m = n
for i in range(m+1):
    for r0, c0 in candi[i]:
        for j in range(i, m+1):
            for r1, c1 in candi[j]:
                if r0==r1 and c0==c1:
                    continue
                if check(r0, c0, i, r1, c1, j) and size < (t:=(4*i+1)*(4*j+1)):
                    size = t
print(size)