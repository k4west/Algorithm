a = open(0)
n = int(next(a))
r = ['No such rule'] + [next(a).strip() for _ in range(n)]
print('\n'.join([f'Rule {i}: {r[i] if 0<i<=n else r[0]}' for i in map(int, a.read().split()[1:])]))