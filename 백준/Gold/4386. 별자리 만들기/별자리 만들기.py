import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def main():
    n = int(input())
    q, stars = [], []
    root = [i for i in range(n)]

    def dist(a, b):
        return (pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)) ** .5

    def find_root(x):
        if x == (t:=root[x]):
            return x
        root[x] = find_root(t)
        return root[x]

    def union_root(x, y):
        if (a:=find_root(x)) == (b:=find_root(y)):
            return False
        if a < b: root[b] = a
        else: root[a] = b
        return True

    for _ in range(n):
        stars.append(tuple(map(float, input().split())))

    for i in range(n-1):
        a = stars[i]
        for j in range(i+1, n):
            heappush(q, (dist(a, stars[j]), i, j))

    cost, c = 0, 1
    while q:
        d, i, j = heappop(q)
        if union_root(i, j):
            cost += d
            c += 1
            if c == n:
                break

    print(f"{cost:.2f}")

if __name__ == "__main__":
    main()