import sys

def main():
    ans = []
    for n in sys.stdin.readlines()[1:]:
        if not (n:=int(n)) in d:
            cnt = 0
            for b in range(2, n + 2):
                s = n
                while not s % b:
                    cnt += 1
                    s //= b
            d[n] = str(cnt)
        ans.append(d[n])
    print("\n".join(ans))

if __name__ == "__main__":
    d = {}
    main()