import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split())
li = sorted(map(int, sys.stdin.readline().split()))
pm = product(map(str, li), repeat=M)
print("\n".join(map(' '.join, pm)))