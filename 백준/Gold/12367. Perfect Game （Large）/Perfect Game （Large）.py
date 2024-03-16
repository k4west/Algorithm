import sys
from functools import cmp_to_key

def minimizing(L, P):
    return L[0] * P[1] - L[1] * P[0]

input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    L = map(int, input().split())
    P = map(int, input().split())
    I = map(str, range(N))
    LPI = sorted(zip(L, P, I), key=cmp_to_key(minimizing))
    print(f"Case #{i+1}: {' '.join((j for _, _, j in LPI))}")