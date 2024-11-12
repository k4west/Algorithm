a = open(0)
t = []
for _ in range(int(next(a))):
    n, *p = map(int, next(a).split())
    v = [0]*17
    for i in range(n):
        r, c = p[2*i:2*i+2]
        v[r] += 1
        v[8+c] += 1
    t.append(['NOT ', ''][set(v)=={0, 1}] + 'SAFE')
print('\n'.join(t))