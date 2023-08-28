import sys
T = int(sys.stdin.readline())
for _ in range(T):
    s = sum(map(int, sys.stdin.readline().split()))
    print(s)