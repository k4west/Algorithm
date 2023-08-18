import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
print("\n".join(list(map(' '.join,product(map(str, range(1,N + 1)), repeat=M)))))