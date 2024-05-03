a = open(0)
L = next(a).rstrip()
for i, G in enumerate(a):
    t = ''
    for l, g in zip(L, G):
        if l == g: t += 'G'
        elif g in L: t += 'Y'
        else: t += 'X'
    if t == 'G'*5: print('WINNER'); break
    elif i < 6: print(t)
    else: print('LOSER')