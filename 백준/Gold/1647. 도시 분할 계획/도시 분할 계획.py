import sys
input = sys.stdin.readline

def find_root(root, n):
    if (nr:=root[n]) == n:
        return n
    root[n] = find_root(root, nr)
    return root[n]

def union_root(root, x, y):
    if x > y:
        root[x] = y
    else:
        root[y] = x
    return

def main():
    N, M = map(int, input().split())
    root = list(range(N+1))
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort(key=lambda x: x[2])
    w, n = 0, 1
    for a, b, c in roads:
        if (x:=find_root(root, a)) == (y:=find_root(root, b)):
            continue
        union_root(root, x, y)
        w += c
        n += 1
        if n == N:
            print(w-c)
            return

if __name__ == "__main__":
    main()