from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
p = [A[0]]

for a in A[1:]:
    if a > p[-1]: p.append(a)
    else:
        for i, b in enumerate(p):
            if a <= b: p[i] = a; break
print(len(p))