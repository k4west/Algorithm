import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))
pm = combinations(li, M)

for p in pm:
    print(*p)