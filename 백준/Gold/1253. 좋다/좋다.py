from sys import stdin
input = stdin.readline


N = int(input())
*A, = map(int, input().split())
A.sort()
good = []

zero = 0 in A
d = {}
for n in A:
    d[n] = d.get(n, 0) + 1

p = 'p'
for i, n in enumerate(A):
    if n == p:
        continue
    s, e = 0, 1
    while s < N-1:
        t = A[s] + A[e]
        if t == n and i not in [s, e]:
            good.append(n)
            p = n
            break
        elif t < n:
            e += 1
        else:
            s += 1
            e = s + 1
        if e == i:
            e += 1
        if e == N:
            s += 1 + (i == s + 1)
            e = s + 1
            if e == i == N-1:
                break

print(sum(d[n] for n in good))
