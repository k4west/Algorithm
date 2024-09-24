N, M, *a = map(int,open(0).read().split())
cb = sorted([a[2*i:2*i+2] for i in range(M)])
s = 0
for c, b in cb:
    if N >= b:
        s += c*b
        N -= b
    else:
        s += c*N
        break
print(s)