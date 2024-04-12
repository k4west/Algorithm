import sys

def main():
    ans = []
    input = sys.stdin.readline
    for _ in range(int(input())):
        cnt = 0
        n = int(input())
        for b in range(2, n + 2):
            s, t = n, b
            while not s % t:
                cnt += 1
                s //= t
        ans.append(cnt)
    print(*ans, sep="\n")

main()