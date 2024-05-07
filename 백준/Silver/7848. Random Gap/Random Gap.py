a, c, m, r = map(int, open(0).read().split())
rn = bytearray(m)
rn[r] = 1
a, c = a%m, c%m
while not rn[r:=(a*r+c)%m]: rn[r] = 1
k, prev = 0, m
for i in range(m):
    if rn[i]:
        if k < (t:=i-prev): k = t
        prev = i
print(k)