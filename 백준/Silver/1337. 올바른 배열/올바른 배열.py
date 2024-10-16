n, *a = map(int, open(0).read().split())
a.sort()
c = 4
for i in range(n-1):
    j = a[i]
    t = 4
    for k in a[i+1:i+5]:
        if j + 4 < k:
            break
        t -= 1
    if c > t:
        c = t
print(c)