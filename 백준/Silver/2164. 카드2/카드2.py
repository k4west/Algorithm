n = int(input())
if n < 3:
    print(n)
else:
    i = n - 1
    c = -1
    while i:
        i //= 2
        c += 1
    print((n - 2**c)*2)