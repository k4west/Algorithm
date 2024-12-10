def main():
    a = open(0)
    n, p, d = map(int, next(a).split())
    pattern = next(a).strip()*2
    c = z = 0
    for i in range(n-p+1, n+n):
        if i > n:
            z -= pattern[i-p] == 'Z'
        z += pattern[i] == 'Z'
        if i >= n:
            c += z < d
    print(c)
main()