import sys
_, X = map(int, sys.stdin.readline().split())
li = map(int, sys.stdin.readline().split())
print(*[i for i in li if i < X])