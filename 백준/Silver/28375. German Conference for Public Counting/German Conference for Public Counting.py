l = len(n := input())
if l > 1:
    a = (l - 1) * 10 + int(n[0])
    if int(n) < int(n[0]) * int("1" * l):
        a -= 1
    print(a)
else:
    print(int(n) + 1)