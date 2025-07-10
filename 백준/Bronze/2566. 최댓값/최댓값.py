M = r = c = 0
for i in range(1, 10):
    for j, n in enumerate(map(int, input().split()), 1):
        if n > M:
            M = n
            r, c = i, j
if M == 0:
    r = c = 1
print(M)
print(r, c)