N, *a = map(int, open(0).read().split())
s = m = 0
counts = [0]*10
num_fruit = 0
for e in range(N):
    if not counts[a[e]]: num_fruit += 1
    counts[a[e]] += 1
    while num_fruit > 2:
        counts[a[s]] -= 1
        if not counts[a[s]]: num_fruit -= 1
        s += 1
    if m < e-s+1: m = e-s+1
print(m)