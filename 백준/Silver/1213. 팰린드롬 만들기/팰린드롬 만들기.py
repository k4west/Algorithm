import sys
s = sys.stdin.readline().rstrip()
d = {a:s.count(a) for a in set(s)}
c = 0
for k, v in d.items():
    if v % 2 != 0:
        c += 1
        u = k
if c > 1:
    r = "I'm Sorry Hansoo"
elif c == 1:
    r = sorted([a*(d[a]//2) for a in set(s)])
    r = "".join(r) + u  + "".join(reversed(r))
else:
    r = sorted([a*(d[a]//2) for a in set(s)])
    r = "".join(r) + "".join(reversed(r))
print(r)