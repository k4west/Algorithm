d = input()
r = 0
for s in d:
    n = ord(s)
    if n <= 83:
        r += min((n-56)//3, 8)
    else: r += min((n-57)//3, 10)
print(r)