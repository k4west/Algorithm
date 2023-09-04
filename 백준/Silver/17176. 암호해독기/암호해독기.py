import sys
sys.stdin.readline()
C = map(int, sys.stdin.readline().split())
P = sys.stdin.readline().strip()

EC = [0] * 53
for c in C:
    EC[c] += 1

k = 1
for p in P:
    p = ord(p)
    p -= [32,64,70][int(p>64)+int(p>96)]
    EC[p] -= 1
    if EC[p] < 0:
        k = 0
        break
print(['n','y'][k])