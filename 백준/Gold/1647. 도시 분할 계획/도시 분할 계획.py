import sys
from itertools import combinations as cb
input = sys.stdin.readline

def find_root(n):
    global root
    if (nr:=root[n]) == n:
        return n
    root[n] = find_root(nr)
    return root[n]

def union_root(a, b):
    global root
    if (x:=find_root(a)) == (y:=find_root(b)):
        return False
    if x > y:
        root[x] = y
    else:
        root[y] = x
    return True

def main():
    ans = float('inf')
    w, n = 0, 1
    for a, b, c in roads:
        if union_root(a, b):
            w += c
            n += 1
        if n == N:
            if ans > w:
                ans = w
            break
    print(ans-c)

if __name__ == "__main__":
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort(key=lambda x: x[2])
    root = list(range(N+1))
    main()