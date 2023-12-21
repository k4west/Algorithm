import sys
input = sys.stdin.readline

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

Tsub = {}
for i in range(n):
    asum = 0
    for j in range(i, n):
        asum += A[j]
        Tsub[asum] = Tsub.get(asum, 0) + 1
    
ans = 0
for i in range(m):
    bsum = 0
    for j in range(i, m):
        bsum += B[j]
        ans += Tsub.get(T-bsum, 0)

print(ans)