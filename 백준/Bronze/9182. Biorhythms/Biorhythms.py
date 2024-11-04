t = []
M = 21252
for n, m in enumerate(open(0)):
    p, e, i, d = map(int, m.split())
    if p == -1:
        break
    t.append(f'Case {n+1}: the next triple peak occurs in {(5544*p+14421*e+1288*i-d)%M or M} days.')
print('\n'.join(t))