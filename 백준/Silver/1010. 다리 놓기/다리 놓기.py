import sys
from math import comb
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(comb(M,N))