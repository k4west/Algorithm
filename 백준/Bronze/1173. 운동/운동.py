def main():
    N, m, M, T, R = map(int, input().split())
    if m + T > M:
        return -1
    t = 0
    n = m
    while N:
        if n + T <= M:
            N -= 1
            n += T
        else:
            n = max(n-R, m)
        t += 1
    return t

if __name__=="__main__":
    print(main())
