def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
t = []
i = open(0)
for _ in range(int(next(i))):
    a, b = map(int, next(i).split())
    d = gcd(a, b)
    t.append("%d %d"%(a*b//d, d))
print('\n'.join(t))