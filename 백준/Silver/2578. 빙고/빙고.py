d = ((-1, 0),  (1, 0), (0, -1), (0, 1))

plate = []
dct = {}
for r in range(5):
    *row, = map(int, input().split())
    plate.append(row)
    for c, n in enumerate(row):
        dct[n] = (r, c)

cnt = 2
for idx, n in enumerate(sum([[*map(int, input().split())] for _ in range(5)], [])):
    r, c = dct[n]
    plate[r][c] = 0
    if idx > 3:
        if not sum(plate[r]):
            cnt -= 1
        if not sum([row[c] for row in plate]):
            cnt -=1
        if r == c and not sum(plate[i][i] for i in range(5)):
            cnt -= 1
        if r+c == 4 and not sum(plate[i][4-i] for i in range(5)):
            cnt -= 1
        if cnt < 0:
            break

print(idx+1)
