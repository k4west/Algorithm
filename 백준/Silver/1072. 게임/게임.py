import sys
X, Y = map(int, sys.stdin.readline().split())
if (Z := (Y * 100) // X) >= 99: print(-1)
else:
    i = (X * (Z + 1) - 100 * Y) // (99 - Z)
    if ((Y + i) * 100) // (X + i) > Z: print(i)
    else: print(i + 1)