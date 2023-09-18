xs, ys = set(), set()
a = open(0)
next(a)
for xy in a:
    x, y = map(int, xy.split())
    xs.add(x)
    ys.add(y)
print((max(xs)-min(xs))*(max(ys)-min(ys)))