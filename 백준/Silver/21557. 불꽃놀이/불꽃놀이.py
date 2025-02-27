def main():
    N, a, *_, b = map(int, open(0).read().split())
    if a>b:a,b=b,a
    if a <= b-N+3:
        return b-N+2
    t = float("inf")
    for i in range(1, (N-1)//2+1):
        c, d = i, N-i-1
        t = min(t, max(a-c, b-d))
    return t
print(main())