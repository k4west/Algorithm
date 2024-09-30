a = open(0)
L, F, M = map(int, input().split())
lead = {}
follow = {}
for _ in range(L):
    k, *d = input().split()
    d = tuple(sorted(d))
    lead[d] = lead.get(d, 0) + 1
for _ in range(F):
    k, *d = input().split()
    d = tuple(sorted(d))
    follow[d] = follow.get(d, 0) + 1
s = 0
for k, v in lead.items():
    s += min(v, follow.get(k, 0)) * len(k) / 3
print(s*M)