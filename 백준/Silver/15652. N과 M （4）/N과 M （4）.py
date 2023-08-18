import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
li = map(str, range(1,N + 1))
cb = combinations_with_replacement(li, M)

for c in cb:
    print(*c)