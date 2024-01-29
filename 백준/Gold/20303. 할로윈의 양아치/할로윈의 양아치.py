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
            friedns[a] += friedns[b]
            candies[a] += candies[b]
        else:
            roots[a] = b
            friedns[b] += friedns[a]
            candies[b] += candies[a]
        return

    input = lambda: map(int, sys.stdin.readline().split())
    N, M, K = input()
    candies = [0] + list(input())
    roots = [i for i in range(N + 1)]
    friedns = [0] + [1 for _ in range(N)]
    roots = [i for i in range(N + 1)]

    for _ in range(M):
        i, j = input()
        union_root(i, j)

    for i in range(1, N + 1):
        find_root(i)

    f_c = [(friedns[i], candies[i]) for i in range(1, N + 1) if i == roots[i]]
    f_c.sort(key=lambda x: (x[0], x[1]))

    dp = [0] * K
    for F, C in f_c:
        for i in range(K - 1, F - 1, -1):
            if dp[i] < (t := dp[i - F] + C):
                dp[i] = t
    print(dp[K - 1])


if __name__ == "__main__":
    main()
