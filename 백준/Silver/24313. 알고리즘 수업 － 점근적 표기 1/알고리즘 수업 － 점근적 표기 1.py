import sys
def f(a1, a0, c, n):
    print("1" if (a1 - c)*n + a0 <= 0 and c >= a1 else 0)
a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())
f(a1, a0, c, n0)


