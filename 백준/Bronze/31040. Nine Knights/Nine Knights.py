d = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
t = []
n = int(input())
for _ in range(n):
    knights = []
    flag=False
    for i in range(5):
        for j, k in enumerate(input()):
            if k=='k':
                knights.append((i, j))
    for i, j in knights:
        for di, dj in d:
            if ((ni:=i+di), (nj:=j+dj)) in knights:
                flag=True
                break
        if flag: break
    t.append('in'*flag+'valid')
    if _: input()
print('\n'.join(t))