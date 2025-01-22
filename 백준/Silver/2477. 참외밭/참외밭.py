n = int(input())
r = [[], [], [], []]
ds = [1, 1, 1, 1]
c = [1, 1]
ph = pl = 0
for _ in range(6):
    d, e = map(int, input().split())
    r[d-1].append(e)
    ds[d-1] ^= 1
    if d > 2:
        if ph == d:
            c[1] = 0
        ph = d
    else:
        if pl == d:
            c[0] = 0
        pl = d
idx = []
for i in range(4):
    if ds[i]:
        idx.append(i)
i, j = idx
M1 = r[i+[1, -1][i%2]][0]
M2 = r[j+[1, -1][j%2]][0]
if c[0]: r[i] = r[i][::-1]
if c[1]: r[j] = r[j][::-1]
if i < 2:
    m1 = r[i][i%2!=j%2]
    m2 = r[j][i%2==j%2]
else:
    m1 = r[i][i%2==j%2]
    m2 = r[j][i%2!=j%2]
print(n*(M1*M2-m1*m2))