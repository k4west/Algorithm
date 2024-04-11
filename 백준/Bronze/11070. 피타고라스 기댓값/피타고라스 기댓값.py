import sys


def main():
    input = sys.stdin.readline
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        ss = [[0, 0] for _ in range(n + 1)]
        for _ in range(m):
            a, b, p, q = map(int, input().split())
            ss[a][0] += p
            ss[a][1] += q
            ss[b][0] += q
            ss[b][1] += p
        W = [s[0] ** 2 / (s[0] ** 2 + s[1] ** 2) if s != [0, 0] else 0 for s in ss[1:]]
        ma, mi = 0, 1
        for w in W:
            if ma < w:
                ma = w
            if mi > w:
                mi = w
        ans.append(int(1000 * ma))
        ans.append(int(1000 * mi))
    print(*ans, sep="\n")


main()