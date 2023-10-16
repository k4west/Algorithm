from sys import stdin
from itertools import combinations_with_replacement
input = stdin.readline

N, M = map(int, input().split())
s = sorted(input().rstrip().split(), key=int)
print("\n".join(map(" ".join, {cm:None for cm in combinations_with_replacement(s, M)})))