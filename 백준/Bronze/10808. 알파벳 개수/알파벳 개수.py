a = [0 for _ in range(26)]
for i in map(ord, input()):
    a[i-97] += 1
print(*a, sep=' ')