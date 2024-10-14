d = (('0', 'O'), ('1', 'L'), ('2', 'Z'), ('3', 'E'), ('5', 'S'), ('6', 'B'), ('7', 'T'), ('8', 'B'))
n, m, *a = open(0).read().split()
n = int(n)
t = []
for i in a[n:]:
    for j, k in d:
        i = i.replace(j, k)
    for p in a[:n]:
        if p.strip() in i:
            t.append('INVALID')
            break
    else:
        t.append('VALID')
print('\n'.join(t))