import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
c = 0
for p in li[::-1]:
    if c < p:
        c = p
    elif c % p:
        c = p*(c//p+1)
print(c)