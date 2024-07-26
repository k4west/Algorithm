n, *m = map(int, open(0).read().split())
pi = 3.14
t = []
for i in range(n):
    a, p1, r, p2 = m[4*i:4*i+4]
    t.append(['Slice of', 'Whole'][a/p1 < r*r*pi/p2] + ' pizza')
print('\n'.join(t))