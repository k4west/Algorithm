from sys import stdin
from itertools import product
input = stdin.readline

N, M = map(int, input().split())
s = sorted(set(input().rstrip().split()), key=int)
print("\n".join(map(" ".join, product(map(str, s), repeat=M))))