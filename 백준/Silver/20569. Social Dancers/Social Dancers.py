a = open(0)
L, F, M = map(int, next(a).split())
lead = [0]*7
follow = [0]*7
nums = [1,1,1,2,2,2,3]
dances = {("bachata",):0, ("country",):1, ("swing",):2, ("bachata", "country"):3, ("bachata", "swing"):4, ("country", "swing"):5, ("bachata", "country", "swing"):6}
for _ in range(L):
    k, *d = sorted(next(a).strip().split())
    lead[dances[tuple(d)]] += 1
for _ in range(F):
    k, *d = sorted(next(a).strip().split())
    follow[dances[tuple(d)]] += 1
s = 0
for i, j, k in zip(lead, follow, nums):
    s += min(i, j) * k / 3
print(s*M)