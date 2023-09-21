import sys
N = int(sys.stdin.readline())
li = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
li.sort(key=lambda x: (x[1], x[0]))

c = 1
e = li[0][1]
for a, b in li[1:N]:
    if e <= a:
        e = b
        c += 1
print(c)