def main():
    a = open(0)
    n, m = map(int, next(a).split())
    for _ in range(m):
        k, *b = map(int, next(a).split())
        for i in (b:=set(b)):
            if -i in b:
                break
        else:
            print('YES')
            print(' '.join(['1' if -j in b else '0' for j in range(1, n+1)]))
            return
    print('NO')
main()