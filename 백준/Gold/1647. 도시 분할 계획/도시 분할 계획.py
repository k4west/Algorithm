import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    root = list(range(N+1))
    roads = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        roads.append((c, a, b))
    roads.sort(key=lambda x: x[0])
    
    def find_root(n):
        if root[n] == n: return n
        root[n] = find_root(root[n])
        return root[n]

    def union_root(x, y):
        if x > y: root[x] = y
        else: root[y] = x
        return
    
    w, n = 0, 1
    for c, a, b in roads:
        if (x:=find_root(a)) == (y:=find_root(b)):
            continue
        union_root(x, y)
        w += c
        n += 1
        if n != N:
            continue
        print(w-c)
        return

if __name__ == "__main__":
    main()