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
        ma, mi = 0, 1000
        for s, a in zip(S[1:], A[1:]):
            if s + a != 0:
                if ma < (w := 1000 * s**2 // (s**2 + a**2)):
                    ma = w
                if mi > w:
                    mi = w
            else:
                mi = 0
        ans.append(ma)
        ans.append(mi)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()