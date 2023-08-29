def isprime(n):
    if n == 1: return 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1

import sys
sys.stdin.readline()
li = map(int, sys.stdin.readline().split())
s = 0
for n in li:
    s += isprime(n)

print(s)