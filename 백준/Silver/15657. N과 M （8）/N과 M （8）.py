import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
li = sorted(map(int, sys.stdin.readline().split()))
cm = combinations_with_replacement(map(str, li), M)
print("\n".join(map(' '.join, cm)))