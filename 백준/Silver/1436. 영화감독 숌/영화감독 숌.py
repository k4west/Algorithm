import sys
N = int(sys.stdin.readline())
s = 666
for _ in range(N-1):
    s += 1
    while "666" not in str(s): s += 1
print(s)