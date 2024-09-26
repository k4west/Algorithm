t = []
for _ in range(int(input())):
    b, x, y = map(int, input().split())
    n = 0
    e = 1
    bt = []
    while x or y:
        n += (x%b+y%b)%b*e
        x //= b
        y //= b
        e *= b
    t.append(n)
print('\n'.join(map(str, t)))