import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append([n%1000 for n in map(int, input().split())])

def mul(a, b):
    return [[sum(i*j%1000 for i, j in zip(ar, br))%1000 for br in zip(*b)] for ar in a]

def bi(a, x):
    if x == 1:
        return a
    if x%2:
        k = bi(a,x//2)
        return mul(a, mul(k, k))
    else:
        k = bi(a,x//2)
        return mul(k, k)

ans = bi(A, B)
print("\n".join(" ".join(map(str, row)) for row in ans))