from sys import stdin
input = stdin.readline
n = int(input())
graph = {}
for _ in range(n):
    p, l, r = input().rstrip().split()
    graph[p] = [l, r]

def rec(s):
    a, b, c = s, s, ""
    for i, t in enumerate(graph[s]):
        if t == ".":
            continue
        x, y, z = rec(t)
        if i%2:
            a += x
            b += y
            c += z
        else:
            a += x
            b = y + b
            c = z
    return a, b, c+s

print("\n".join(rec("A")))