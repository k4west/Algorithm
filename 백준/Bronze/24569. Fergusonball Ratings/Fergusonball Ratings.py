a = open(0)
n = int(next(a))
t = 0
for i in range(n):
    s, c = map(int, (next(a), next(a)))
    if 5*s-3*c > 40:
        t += 1
print(t, '+'*(n==t), sep='')