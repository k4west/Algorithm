import sys
input = sys.stdin.readline
from math import comb

N, K = map(int, input().split())
print(comb(N,K))
