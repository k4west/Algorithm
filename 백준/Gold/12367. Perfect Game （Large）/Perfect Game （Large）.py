import sys
from functools import cmp_to_key
def minimizing(L, P):
    return L[0] * P[1] - L[1] * P[0]
ans = []
input = sys.stdin.readline
for i in range(int(input())):
    N = int(input())
    ans.append(f"Case #{i+1}: {' '.join((j for _, _, j in sorted(list(zip(map(int, input().split()), map(int, input().split()), map(str, range(N)))), key=cmp_to_key(minimizing))))}")
print('\n'.join(ans))