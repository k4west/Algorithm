import sys
_, a, b = map(int, sys.stdin.readline().split())
c = 1
while a != b:
    a -= a//2
    b -= b//2
    if a == b:
        print(c)
    c += 1