a = b = 0
for n, p in zip(tuple(map(int, input().split())), (1, 5, 10, 20, 50, 100)):
    if b <= (t:= n * p): a, b = p, t
print(a)