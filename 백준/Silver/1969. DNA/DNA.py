import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = [{"A": 0, "C": 0, "G": 0, "T": 0} for _ in range(M)]
for _ in range(N):
    for i, s in enumerate(input().rstrip()):
        dna[i][s] += 1

ans = ""
for d in dna:
    ts, tc = '', 0
    for s, c in d.items():
        if c > tc:
            ts, tc = s, c
    ans += ts

c0 = 0
for s0, d in zip(ans, dna):
    for s, c in d.items():
        if s != s0:
            c0 += c

print(ans)
print(c0)