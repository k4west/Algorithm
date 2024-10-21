m = 10**9 + 7
s = 0
H, x, *a = map(int, open(0).read().split())
for i in a[::-1]:
    s = ((s+i)*x)%m
print(s)