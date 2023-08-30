input()
s, r, M = 0, 31, 1234567891
for i, n in enumerate(input()):
    s += (ord(n)-96)*(r**i)%M
print(s)