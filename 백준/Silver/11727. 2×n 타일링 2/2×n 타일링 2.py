n = int(input())
i = j = 1
for _ in range(n-1):
    i, j = j, (2*i + j) % 10007
print(j)