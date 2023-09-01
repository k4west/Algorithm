import sys
sys.stdin.readline()
c, *li = map(int, sys.stdin.readline().split())
li.sort()
for a in li:
    if c <= a:
        print('No')
        exit()
    c += a
print('Yes')