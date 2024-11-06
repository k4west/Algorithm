t = []
for _ in range(int(input())):
    g, c, e = map(int, input().split())
    t.append((2*g-1)*max(0, (e-c)))
print(*t, sep='\n')