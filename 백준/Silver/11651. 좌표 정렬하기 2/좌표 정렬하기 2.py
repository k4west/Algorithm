import sys
T = int(sys.stdin.readline())
li = []
for _ in range(T):
    xy = list(map(int, sys.stdin.readline().strip().split()))
    li.append(xy)
li = sorted(li, key=lambda x: (x[1], x[0]))
for xy in li:
    print(*xy)