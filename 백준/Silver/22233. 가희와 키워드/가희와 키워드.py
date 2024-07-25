nm, *a= open(0)
n, m = map(int, nm.split())
s = set(map(lambda x: x.strip(), a[:n]))
t = []
for i in a[n:]:
    s-=set(i.strip().split(','))
    t.append(len(s))
print('\n'.join(map(str, t)))