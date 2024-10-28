n, *a = open(0)
t = []
v = set('aeiouy')
for i in a:
    k, s = i.rstrip().split()
    k = int(k)
    c = p = 0
    for j in s:
        if j in v:
            c += 1
        else:
            c = 0
        if c >= k:
            p += 1
    t.append(p)
print('\n'.join(map(str, t)))