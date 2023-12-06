import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]

def find_root(r):
    nr = parent[r]
    while nr != r:
        pr, r, nr = r, nr, parent[nr]
        parent[pr] = nr
    return r

w, v = 0, 0
for a, b, c in graph:
    if (x:=find_root(a)) == (y:=find_root(b)):
        continue
    parent[y] = x
    w += c
    v += 1
    if v == V-1:
        break
print(w)