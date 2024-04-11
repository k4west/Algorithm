l = len(n := input())
if l > 1:
    a = (l - 1) * 10 + int(n[0])
    if n < n[0] * l: a -= 1
    print(a)
else: print(int(n) + 1)