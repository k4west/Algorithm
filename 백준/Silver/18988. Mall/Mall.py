def main():
    nm, *a = open(0)
    n, m = map(int, nm.split())
    shops = []
    products = [[] for _ in range(m+1)]
    results = [0] * (m+1)
    for i, j in enumerate(a, 1):
        tmp = []
        for k in [*map(int, j.split())][1:]:
            tmp.append(k)
            products[k].append(i)
        shops.append(tmp)

    for i, j in enumerate(shops, 1): 
        for k in j:
            if len(products[k]) == 1:
                results[k] = i
            else:
                idx = products[k].index(i)
                products[k].pop(idx)

    if all(results[1:]):
        print('YES')
        print(*range(1,n+1), sep=' ')
        print(*results[1:], sep=' ')
    else:
        print('NO')
main()