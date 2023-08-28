import sys
while 1:
    s = sum(map(int, sys.stdin.readline().split()))
    if s:
        print(s)
    else: break