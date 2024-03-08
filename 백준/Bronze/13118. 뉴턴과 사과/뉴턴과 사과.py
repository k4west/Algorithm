import sys
input = sys.stdin.readline
ps = input().rstrip().split()
x, i = input().split()[0], 1
for p in ps:
    if p == x: break
    i += 1
print(i%5)