import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def subsum(N, L):
    Lsub = []
    for i in range(N):
        ss = 0
        for j in range(i, N):
            ss += L[j]
            Lsub.append(ss)
    return sorted(Lsub)

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

Asub, Bsub = subsum(n, A), subsum(m, B)
ans = 0
for asub in Asub:
    tmp = T - asub
    l, r = bisect_left(Bsub, tmp), bisect_right(Bsub, tmp)
    ans += r-l

print(ans)