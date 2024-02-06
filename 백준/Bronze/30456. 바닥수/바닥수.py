import sys

N, L = map(int, sys.stdin.readline().split())
print("".join(map(str, [1]*(L-1) + [N])))