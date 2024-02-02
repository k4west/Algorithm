import sys
from heapq import heapify, heappop

input()
input = lambda: map(int, sys.stdin.readline().split())

A = list(input())
heapify(A)
B = input()

S = 0
for b in sorted(B, reverse=True):
    S += heappop(A) * b
print(S)