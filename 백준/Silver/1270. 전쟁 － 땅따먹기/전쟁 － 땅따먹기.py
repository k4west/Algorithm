from sys import stdin
from collections import Counter
input = stdin.readline
ans = []
ing = "SYJKGW"
for _ in range(int(input())):
    t, *li = input().rstrip().split()
    a, b = Counter(li).most_common(n=1)[0]
    if b > int(t) / 2: ans.append(a)
    else: ans.append(ing)
print("\n".join(ans))