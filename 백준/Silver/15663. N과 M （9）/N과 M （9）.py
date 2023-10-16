from sys import stdin
from itertools import permutations
input = stdin.readline

N, M = map(int, input().split())
s = sorted(map(int, input().split()))
pms = permutations(s, M)
d = {pm:pm for pm in pms}
for pm in d:
    print(*pm)