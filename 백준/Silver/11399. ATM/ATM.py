import sys
def f(N):
    li = sorted(map(int, sys.stdin.readline().split()))
    return sum([t*(N-i) for i, t in enumerate(li)])
N = int(sys.stdin.readline())
print(f(N))