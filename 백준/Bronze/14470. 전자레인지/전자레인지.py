a, b, c, d, e = map(int, open(0).read().split())
if a < 0:
    t = -a*c+d+b*e
else:
    t = (b-a)*e+(not a)*d
print(t)