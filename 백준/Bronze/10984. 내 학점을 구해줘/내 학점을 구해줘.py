a = []
i = open(0)
for _ in range(int(next(i))):
    s = t = 0
    for _ in range(int(next(i))):
        c, g = map(float,next(i).split())
        s += c
        t += g*c
    a.append(f'{int(s)} {t/s:.1f}')
print('\n'.join(a))