import sys
sys.stdin.readline()
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 0
xs = [0]
ys = [0]
orders = sys.stdin.readline().strip()
for order in orders:
    if order == "R":
        d += 1
    elif order == "L":
        d -= 1
    else:
        x, y = xs[-1], ys[-1]
        dx, dy = direction[d%4]
        xs.append(x + dx)
        ys.append(y + dy)
x0, y0 = min(xs), min(ys)
x1, y1 = max(xs), max(ys)
h, w = x1 - x0 + 1, y1 - y0 + 1
A = [["#"]*w for _ in range(h)]
for x, y in zip(xs, ys):
    x -= x0
    y -= y0
    A[x][y] = '.'
for row in A:
    print(*row, sep="")