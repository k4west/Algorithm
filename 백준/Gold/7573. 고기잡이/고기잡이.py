N, I, M = map(int, input().split())
fishes = {}
xs = set()
ys = set()
for _ in range(M):
    r, c = map(int, input().split())
    xs.add(r)
    ys.add(c)
    if r in fishes:
        fishes[r].append(c)
    else:
        fishes[r] = [c]

for r in fishes.keys():
    fishes[r].sort()
xs = sorted(xs)
ys = sorted(ys)

max_count = 0
for width in range(1, I//2):
    height = I//2-width
    for x in xs:
        for y in ys:
            count = 0
            for x1 in range(x, x+width+1):
                for y1 in fishes.get(x1, []):
                    if 0 <= y1 - y <= height:
                        count += 1
            if max_count < count:
                max_count = count
print(max_count)