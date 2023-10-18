import sys
s = sys.stdin.readline()
print(max(s.count('01'), s.count('10')))