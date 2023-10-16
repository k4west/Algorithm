from sys import stdin
from itertools import combinations_with_replacement
input = stdin.readline

N, M = map(int, input().split())
s = sorted(set(input().rstrip().split()), key=int)
print("\n".join(map(" ".join, combinations_with_replacement(map(str, s), M))))