N, I, M = map(int, input().split())
fishes = []
xs = set()
ys = set()
for _ in range(M):
    r, c = map(int, input().split())
    fishes.append((r, c))
    xs.add(r)
    ys.add(c)

fishes.sort()
xs = sorted(xs)
ys = sorted(ys)

max_count = 0
for width in range(1, I//2):
    height = I//2-width
    for x in xs:
        for y in ys:
            count = 0
            for i, j in fishes:
                if 0 <= i - x <= width and 0 <= j - y <= height:
                    count += 1
            if max_count < count:
                max_count = count
print(max_count)
