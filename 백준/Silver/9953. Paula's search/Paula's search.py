def f(n):
    c, s, e = 0, 0, 49
    while True:
        c += 1
        m = (s+e)//2
        if m > n: e = m-1
        elif m < n: s = m+1
        else: break
    return c
print(*[str(f((n-1)//2) + n%2) for i in open(0) if (n:=int(i))])