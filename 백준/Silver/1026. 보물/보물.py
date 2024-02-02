import sys

input()
input = lambda: sorted((map(int, sys.stdin.readline().split())))

A = input()
B = input()

S = 0
for a, b in zip(A[::-1], B):
    S += a*b

print(S)