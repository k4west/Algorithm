import sys
s=sys.stdin.readline().strip()
print(s.count(" ")+1 if s else 0)