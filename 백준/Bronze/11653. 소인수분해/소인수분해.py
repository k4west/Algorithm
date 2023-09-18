N = int(input())
m = N
t = []
for n in range(2, N+1):
    c = 0
    while not m%n:
        c += 1
        m //= n
    t.extend([n]*c)
print(*t, sep='\n')