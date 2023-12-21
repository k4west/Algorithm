import sys
input = sys.stdin.readline

def subsum(N, L):
    Lsub = {}
    for i in range(N):
        ss = 0
        for j in range(i, N):
            ss += L[j]
            Lsub[ss] = Lsub.get(ss, 0) + 1
    return Lsub

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

Asub, Bsub = subsum(n, A), subsum(m, B)
ans = 0
for asub, an in Asub.items():
    tmp = T - asub
    ans += an*Bsub.get(tmp, 0)

print(ans)