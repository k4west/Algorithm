N, *a = map(int, open(0).read().split())
s = m = 0
counts = [0]*10
tanghuru = [0]*10
num_fruit = 0
for e in range(N):
    counts[a[e]] += 1
    tanghuru[a[e]] = 1
    while sum(tanghuru) > 2:
        counts[a[s]] -= 1
        if not counts[a[s]]:tanghuru[a[s]] = 0
        s += 1
    if m < e-s+1:
        m = e-s+1
print(m)