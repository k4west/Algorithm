X = int(input())
count = 0
def sa(X):
    k = list(map(int,str(X)))
    n = len(k)
    return k, n - 1
for x in range(1, X + 1):
    if (x / 100) < 1 :
        count += 1
    else:
        k, n = sa(x)
        c = 0
        for i, j in zip(k[0:-1], k[1:]):
            if (k[0] - k[1]) == (i - j):
                c += 1
        count += int(c / n)
print(count)