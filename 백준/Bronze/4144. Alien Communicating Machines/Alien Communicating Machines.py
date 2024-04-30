d = {i: str(i) for i in range(10)}
for i in range(65, 91): d[i - 55] = chr(i)
a = open(0)
for _ in range(int(next(a))):
    x, y, z = next(a).split()
    z = int(z, int(x))
    if not z: print(0)
    else:
        y = int(y)
        tmp = ""
        while z:
            tmp += d[z % y]
            z //= y
        print(tmp[::-1])