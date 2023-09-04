import sys
sys.stdin.readline()
C = map(int, sys.stdin.readline().split())
P = sys.stdin.readline().strip()

EC = {}
for c in C:
    c += [32,64,70][int(c>0)+int(c>26)]
    c = chr(c)
    EC[c] = EC.get(c, 0) + 1

k = 1
for p in P:
    if p not in EC or EC[p] == 0:
        k = 0 
        break
    EC[p] -= 1
print(['n','y'][k])