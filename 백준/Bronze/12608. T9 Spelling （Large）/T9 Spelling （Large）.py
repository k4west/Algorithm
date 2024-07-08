d = {chr(i+97):f'{(i-(i//18))//3+2}'*((i-(i//18))%3+1) for i in range(25) if i != 18}
d.update({'s': '7777', 'z': '9999', ' ': '0'})

tmp = []
for i in range(int(input())):
    s = ' '
    for w in input():
        t = d[w]
        if s[-1] == t[0]:
            s += ' '
        s += t
    tmp.append(f'Case #{i+1}:{s}')
print('\n'.join(tmp))