import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0, 0)
    sys.exit()
row, col = [[] for _ in range(N)], [[] for _ in range(N)]

for i in range(N):
    for j, k in enumerate(input().rstrip()):
        if k == 'X':
            row[i].append(j)
            col[j].append(i)

def f(room):
    c = 0
    for r in room:
        r.append(N)
        s = -1
        for x in r:
            if x-s > 2:
                c += 1
            s = x
    return c

print(f(row), f(col))