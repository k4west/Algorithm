a = open(0)
d = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
t = []
n = int(next(a))
for _ in range(n):
    knights = []
    flag=False
    for i in range(5):
        for j, k in enumerate(next(a).strip()):
            if k=='k':
                knights.append((i, j))
    for i, j in knights:
        for di, dj in d:
            if ((ni:=i+di), (nj:=j+dj)) in knights:
                flag=True
                break
        if flag: break
    t.append('in'*flag+'valid')
    if _: next(a)
print('\n'.join(t))