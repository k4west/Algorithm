import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
    n = float(sys.stdin.readline())
    if len(li) < 7:
        li.append(n)
        li.sort()
    else:
        if n < li[6]:
            li[6] = n
            li.sort()
for n in li:
    print(f"{n:.3f}")