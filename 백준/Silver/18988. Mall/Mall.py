def main():
    nm, *a = open(0)
    n, m = map(int, nm.split())
    products = [[] for _ in range(m+1)]
    for i, j in enumerate(a, 1):
        for k in [*map(int, j.split())][1:]:
            products[k].append(i)
    if all(products[1:]):
        print('YES')
        print(*range(1,n+1), sep=' ')
        print(*[products[i][-1] for i in range(1, m+1)], sep=' ')
    else:
        print('NO')
main()