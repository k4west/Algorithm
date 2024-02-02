import sys

n = sys.stdin.readline()
d = {i: n.count(i) for i in map(str, range(9, -1, -1))}
print("".join((i * j for i, j in d.items())))