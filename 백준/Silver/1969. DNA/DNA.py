import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = [{"A": 0, "C": 0, "G": 0, "T": 0} for _ in range(M)]
for _ in range(N):
    for i, s in enumerate(input().rstrip()):
        dna[i][s] += 1

ans, hd = "", 0
for d in dna:
    ts, tc, td = '', 0, []
    for s, c in d.items():
        td.append((s, c))
        if c > tc:
            ts, tc = s, c
    ans += ts
    hd += N-tc

print(ans)
print(hd)