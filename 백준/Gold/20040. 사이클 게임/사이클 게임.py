import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    root = list(range(n))
    ans = 0

    def find_root(x):
        if (k:=root[x]) == x:
            return x
        root[x] = find_root(k)
        return root[x]

    def union_root(a, b):
        x, y = find_root(a), find_root(b)
        if x == y:
            return True
        if a < b:
            root[y] = a
        else:
            root[x] = b
        return False

    for i in range(m):
        a, b = map(int, input().split())
        if union_root(a, b):
            ans = i+1
            break

    print(ans)

if __name__ == "__main__":
    main()