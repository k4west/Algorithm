import sys
m = [0,0]
for i in range(1, 10):
    n = int(sys.stdin.readline())
    if n > m[0]:
        m = [n,i]
print(*m, sep="\n")