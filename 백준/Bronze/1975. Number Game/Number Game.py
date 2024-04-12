import sys

def main():
    ans = []
    d = {}
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        if n in d:
            cnt = d[n]
        else:
            cnt = 0
            for b in range(2, n + 2):
                s, t = n, b
                while not s % t:
                    cnt += 1
                    s //= t
            d[n] = cnt
        ans.append(cnt)
    print(*ans, sep="\n")

main()