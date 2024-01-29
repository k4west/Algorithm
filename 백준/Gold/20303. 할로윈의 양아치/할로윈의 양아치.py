import sys

def main():
    def find_root(x):
        if x == (t := roots[x]):
            return x
        roots[x] = find_root(t)
        return roots[x]


    def union_root(x, y):
        if (a := find_root(x)) == (b := find_root(y)):
            return
        if a < b:
            roots[b] = a
        else:
            roots[a] = b
        return


    input = lambda: map(int, sys.stdin.readline().split())
    N, M, K = input()
    candies = list(input())
    friends = [tuple(input()) for _ in range(M)]
    roots = [i for i in range(N + 1)]

    for i, j in friends:
        union_root(i, j)

    for i in range(1, N+1):
        find_root(i)

    d = {root: [0, 0] for root in roots}
    for i, root in enumerate(roots[1:]):
        d[root][0] += 1
        d[root][1] += candies[i]

    dp = {0: 0}
    for F, C in d.values():
        tmp = {}
        for f, c in dp.items():
            if (f := F + f) >= K:
                continue
            if dp.get(f, 0) < (c := C + c):
                tmp[f] = c
        dp.update(tmp)
    print(max(dp.values()))

if __name__ == "__main__":
    main()
    