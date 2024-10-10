a = set([int(x) for x in input().split()][1:])
b = set([int(x) for x in input().split()][1:])
n, m, t = 0, 0, 0
for i in range(1000000):
    if i in a and i in b:
        t += 1
        n, m = 0, 0
    elif i in a and m == 0:
        t += 1
        m += 1
        n = 0
    elif i in b and n == 0:
        t += 1
        n += 1
        m = 0
print(t)