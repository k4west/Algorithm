N = int(input())
ranks = [1 for _ in range(N)]
people = [[*map(int, input().split())]+[i] for i in range(N)]
people.sort(key=lambda x:(-x[0], -x[1]))

for i, (w, h, o) in enumerate(people):
    c = 0
    for w1, h1, _ in people[:i]:
        if w!=w1 and h < h1:
            c += 1
    ranks[o] += c
print(*ranks)