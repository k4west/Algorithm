import sys
input = sys.stdin.readline

def find_root(root, n):
    if (nr:=root[n]) == n:
        return n
    root[n] = find_root(root, nr)
    return root[n]

def union_root(root, a, b):
    if (x:=find_root(root, a)) == (y:=find_root(root, b)):
        return False
    if x > y:
        root[x] = y
    else:
        root[y] = x
    return True

def main():
    N, M = map(int, input().split())
    root = list(range(N+1))
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort(key=lambda x: x[2])
    ans = float('inf')
    w, n = 0, 1
    for a, b, c in roads:
        if union_root(root, a, b):
            w += c
            n += 1
        if n == N:
            if ans > w:
                ans = w
            break
    print(ans-c)

if __name__ == "__main__":
    main()