import sys
input = sys.stdin.readline
mod = 1_000_000_007
M = int(input())
ans = []

def sum_frac(a, b, c, d):
    return (a*d+b*c)%mod, b*d%mod

def irr_frac(A, B):
    q, r = A, B
    while q%r:
        q, r = r, q%r
    return A//r, B//r

def inverse(b, x=mod-2):
    if x == 1:
        return b
    if x%2:
        return (b*pow(inverse(b, x//2), 2, mod)) % mod
    else:
        return pow(inverse(b, x//2), 2, mod)

b, a = map(int, input().split())
for _ in range(M-1):
    N, S = map(int, input().split())
    a, b = sum_frac(a, b, S, N)
A, B = irr_frac(a, b)
print(((A%mod)*(inverse(B)%mod)) % mod)
