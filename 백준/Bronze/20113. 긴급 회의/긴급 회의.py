N, *votes = map(int, open(0).read().split())
result = [0 for _ in range(N+1)]
for v in votes:
    result[v] += 1
idx = []
mv = 0

for i, v in enumerate(result[1:], 1):
    if mv < v:
        mv = v
        idx = [i]
    elif mv == v:
        idx.append(i)
if len(idx) == 1:
    print(idx[0])
else:
    print("skipped")