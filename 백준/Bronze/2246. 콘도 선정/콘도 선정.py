n, *a = open(0)
n = int(n)
t = 0
condo = [[*map(int, i.split())] for i in a]
dc = sorted(condo, key=lambda x: x[0])
cd = sorted(condo, key=lambda x: x[1])
for i in range(n):
    d0, c0 = condo[i]
    f1 = f2 = True
    for d1, c1 in dc:
        if d0 <= d1: break
        elif c0 >= c1: 
            f1 = False
            break
    if f1:
        for d1, c1 in cd:
            if c0 <= c1: break
            elif d0 >= d1: 
                f2 = False
                break
    if f1 and f2:
        t += 1
print(t)