i, n = 0, 1
N = int(input())
while N:
    if N < n:
        n = 1
    N -= n
    n += 1
    i += 1
print(i)