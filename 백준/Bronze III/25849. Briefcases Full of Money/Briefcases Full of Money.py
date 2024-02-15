import sys

a = b = 0
for n, p in zip(tuple(map(int, sys.stdin.readline().split())), (1, 5, 10, 20, 50, 100)):
    if b <= (n * p):
        b = n * p
        a = p
print(a)