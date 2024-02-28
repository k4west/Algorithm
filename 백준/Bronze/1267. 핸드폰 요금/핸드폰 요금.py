d = {'Y': 0, 'M': 0}
input()
for n in map(int, input().split()):
    d['Y'] += 10 * (n // 30 + 1)
    d['M'] += 15 * (n // 60 + 1)
if d['Y'] == d['M']: print(f'Y M {d["Y"]}')
elif d['Y'] < d['M']: print(f'Y {d["Y"]}')
else: print(f'M {d["M"]}')