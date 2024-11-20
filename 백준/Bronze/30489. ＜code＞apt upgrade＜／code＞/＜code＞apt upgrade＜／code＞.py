def main():
    a = open(0)
    n, m, k = map(int, next(a).split())
    s = sorted(map(int, next(a).split()), reverse=True)
    total = sum(s)
    print((sum(s[:m]) + sum(s[m:m+k]))/total * 100)
main()