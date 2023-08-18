import sys
from math import comb
input = sys.stdin.readline()

n = int(input.strip())

q = n // 2
p = 0
answer = 0

while p <= q:
    answer += comb(n + p, p)    
    p += 1
    n -= 2

print(answer % 10007)