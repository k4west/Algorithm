n = int(input())
t = 0
for i in range(2, n+1):
    for j in range(2, int(i ** .5) + 1):
        if i % j == 0:
            t += 1
print(t+n)
