import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def subsum(N, L):
    Lsub = []
    for i in range(N):
        for j in range(i+1, N+1):
            Lsub.append(sum(L[i:j]))
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