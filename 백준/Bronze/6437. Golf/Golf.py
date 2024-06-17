ans = []
d = {-2: 'Double Bogey', -1: 'Bogey', 0: 'Par', 1: 'Birdie', 2: 'Eagle', 3: 'Double eagle', 4: 'Double eagle'}
for i, a in enumerate(open(0).readlines(), 1):
    p, s = map(int, a.split())
    if s == 0:
        break
    elif s == 1:
        t = 'Hole-in-one'
    else:
        t = d[max(p-s, -2)]
    ans.append(f'Hole #{i}\n{t}.')
print('\n\n'.join(ans))