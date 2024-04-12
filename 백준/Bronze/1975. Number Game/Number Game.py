import sys

def main():
    ans = []
    d = {}
    for n in sys.stdin.readlines()[1:]:
        if (n:=int(n)) in d:
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
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()