def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    s = {}
    for i in range(N):
        if (n:= input().rstrip()) in s: s[n] += 1
        else: s[n] = 1
    for n in map(str, range(1, 10001)):
        if n in s:
            for _ in range(s[n]): sys.stdout.write(n+"\n")

if __name__ == "__main__":
    main()