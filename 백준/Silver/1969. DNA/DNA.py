import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = [input().rstrip() for _ in range(N)]
d, ss = {"A": 0, "C": 0, "G": 0, "T": 0}, 'ACGT'

def f():
    ans, hd = "", 0
    for i in range(M):
        for j in range(N):
            d[dna[j][i]] += 1
        
        ts, tc = '', 0
        for s in ss:
            if (c:=d[s]) > tc:
                ts, tc = s, c
            d[s] = 0

        ans += ts
        hd += N-tc

    print(ans, hd, sep='\n')

f()