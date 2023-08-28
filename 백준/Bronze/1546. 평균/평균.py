import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
print((100*sum(s))/(n*max(s)))