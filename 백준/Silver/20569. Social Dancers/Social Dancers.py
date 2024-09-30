a = open(0)
dances = {("bachata",):0, ("country",):1, ("swing",):2, ("bachata", "country"):3, ("bachata", "swing"):4, ("country", "swing"):5, ("bachata", "country", "swing"):6}
def f(n):
    li = [0]*7
    for _ in range(n):_, *d = sorted(next(a).strip().split());li[dances[tuple(d)]] += 1
    return li
L, F, M = map(int, next(a).split())
s = 0
for i, j, k in zip(f(L), f(F), [1,1,1,2,2,2,3]):s += min(i, j) * k / 3
print(s*M)