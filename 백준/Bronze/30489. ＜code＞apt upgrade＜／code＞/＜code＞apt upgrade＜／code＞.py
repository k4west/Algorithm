def main():
    a = open(0)
    n, m, k = map(int, next(a).split())
    s = sorted(map(int, next(a).split()), reverse=True)
    print(sum(s[:m+k])/sum(s) * 100)
main()