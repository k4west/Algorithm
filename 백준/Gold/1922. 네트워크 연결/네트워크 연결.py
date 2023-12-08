import sys
input = sys.stdin.readline
def main():
    V = int(input())
    E = int(input())
    graph = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    graph.sort(key=lambda x: x[0])
    parent = [i for i in range(V+1)]

    def find_root(r):
        nr = parent[r]
        while nr != r:
            pr, r, nr = r, nr, parent[nr]
            parent[pr] = nr
        return r

    def union_root(a, b):
        if (x:=find_root(a)) == (y:=find_root(b)):
            return False
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
        return True
            
    w, v = 0, 0
    for c, a, b in graph:
        if union_root(a, b):
            w += c
            v += 1
            if v == V-1:
                break
    print(w)

if __name__ == "__main__":
    main()