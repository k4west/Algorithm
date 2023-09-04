import sys
li = map(int, sys.stdin.readline().split())
n, m = 0, []
for c in li:
    q, r = c//3, c%3
    n += q
    if r:
        m.append(r)
if len(m) == 1:
    n += 1
elif len(m) > 1:
    n+=max(m)
print(n)