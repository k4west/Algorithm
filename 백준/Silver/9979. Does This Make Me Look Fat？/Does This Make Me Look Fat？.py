import sys
from heapq import heappop, heappush

string = sys.stdin.readlines()
ans, order = [], []

for s in string:
    s = s.rstrip()
    if s == "START":
        continue
    if s == "END":
        while order:
            ans.append(heappop(order)[1])
        ans.append("")
        continue
    name, d, w = s.split()
    heappush(order, (int(d) - int(w), name))

print("\n".join(ans[:-1]))