def gcd(a,b):
    while b!=0:
        r = a%b
        a, b = b, r
    return a

import sys
a,b = map(int, sys.stdin.readline().split())
print(gcd(a,b))
print(a*b//gcd(a,b))