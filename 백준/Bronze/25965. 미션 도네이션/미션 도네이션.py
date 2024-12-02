a = iter(map(int, open(0).read().split()))
t = []
for _ in range(int(next(a))):
    m = int(next(a))
    *ms, k, d, a_  = [int(next(a)) for _ in range(m*3+3)]
    t.append(sum(max(0, sum([(-1)**i*j*k for i, (j, k) in enumerate(zip(ms[3*idx:3*idx+3], (k, d, a_)))])) for idx in range(m)))
print('\n'.join(map(str, t)))