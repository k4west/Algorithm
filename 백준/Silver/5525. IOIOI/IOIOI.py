import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
s = sys.stdin.readline()
P_N, c = 'IO'*N+'I', 0
N *= 2
for i in range(M-N):
    if s[i:i+N+1] == P_N:
        c += 1
print(c)