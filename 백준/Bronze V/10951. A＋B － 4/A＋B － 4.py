ans = []
for a in open(0):
    ans.append(sum(map(int, a.split())))
print("\n".join(map(str, ans)))