import sys
input = sys.stdin.readline
ans = []
for t in range(int(input())):
    d = {}
    contestants = []
    for _ in range(int(input())):
        name_year = input().rstrip()
        name = name_year[:-5]
        year = name_year[-4:]
        if name in d: d[name].add(year)
        else: d[name] = {year}
    for name, years in d.items():
        if len(years) < 5: contestants.append(name)
    tmp = [f"Case #{t+1}:"] + sorted(contestants)
    ans.append("\n".join(tmp))
print("\n".join(ans))