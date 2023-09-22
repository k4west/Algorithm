import sys
def f():
    a, b = map(int, sys.stdin.readline().split())
    for i in range(min(a,b), 0, -1):
        if a%i + b%i == 0:
            return a*b//i
N = int(sys.stdin.readline())
for _ in range(N):
    print(f())