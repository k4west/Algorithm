o = open(0)
t = []
xs = [3, 15, 120, 528, 4095, 17955, 139128, 609960, 4726275, 20720703, 160554240, 703893960]
idx = 1
while True:
    a, b = map(int, next(o).split())
    if a == b == 0:
        break
    c = 0
    for i in xs:
        c += a <= i < b-1
    t.append(f"Case {idx}: {c}")
    idx += 1
print('\n'.join(t))