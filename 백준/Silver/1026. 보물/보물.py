import sys
from heapq import heappush, heappop

input()
input = lambda: map(int, sys.stdin.readline().split())

A = []
for a in input():
    heappush(A, a)
B = input()

S = 0
for b in sorted(B, reverse=True):
    S += heappop(A) * b
print(S)