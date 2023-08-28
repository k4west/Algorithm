import sys
B = set(range(1,31))
C = set()
for _ in range(28):
    C.add(int(sys.stdin.readline().rstrip()))
print(*sorted(set.difference(B,C)), sep="\n")