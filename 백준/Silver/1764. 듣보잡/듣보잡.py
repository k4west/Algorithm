import sys
N, M = map(int, sys.stdin.readline().split())
s1 = {sys.stdin.readline().rstrip() for _ in range(N)}
s2 = set()
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if name in s1:
        s2.add(name)
print(len(s2))
print("\n".join(sorted(s2)))