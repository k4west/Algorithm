t = 0
for s in input():
    n = ord(s) - 56
    if n >= 27:
        n -= 1
    if n == 33:
        n -= 1
    t += n // 3
print(t)