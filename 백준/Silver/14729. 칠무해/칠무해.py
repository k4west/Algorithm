import sys
N = int(sys.stdin.readline())
li = []
for i in range(7):
    n = float(sys.stdin.readline())
    li.append(n)
li.sort()
for i in range(7, N):
    n = float(sys.stdin.readline())
    if n < li[6]:
        li[6] = n
        li.sort()
for n in li:
    print(f"{n:.3f}")