from sys import stdin
from itertools import permutations
input = stdin.readline

N, M = map(int, input().split())
s = sorted(input().rstrip().split(), key=int)
print("\n".join(map(" ".join, dict.fromkeys(permutations(s, M)))))