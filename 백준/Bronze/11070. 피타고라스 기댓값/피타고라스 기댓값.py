import sys


def main():
    input = sys.stdin.readline
    ans = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        S = [0 for _ in range(n + 1)]
        A = [0 for _ in range(n + 1)]
        for _ in range(m):
            a, b, p, q = map(int, input().split())
            S[a] += p
            A[a] += q
            S[b] += q
            A[b] += p
        W = [s ** 2 / (s ** 2 + a ** 2) if s + a != 0 else 0 for s, a in zip(S[1:], A[1:])]
        ma, mi = 0, 1
        for w in W:
            if ma < w:
                ma = w
            if mi > w:
                mi = w
        ans.append(int(1000 * ma))
        ans.append(int(1000 * mi))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()