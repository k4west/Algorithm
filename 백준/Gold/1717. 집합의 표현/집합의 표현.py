from sys import stdin


def find(x):
    tmp = []
    while x != roots[x]:
        tmp.append(x)
        x = roots[x]
    
    for px in tmp:
        roots[px] = x

    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a

    roots[b] = a


input = stdin.readline

ans = []
n, m = map(int, input().split())
*roots, = range(n+1)
options = ["NO", "YES"]

for _ in range(m):
    op, a, b = map(int, input().split())
    if not op:
        union(a, b)
    else:
        ans.append(options[find(a) == find(b)])

print("\n".join(ans))
