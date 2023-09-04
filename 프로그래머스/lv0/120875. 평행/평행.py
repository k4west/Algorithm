def solution(dots):
    a,b,c,d = dots
    m1 = (a[1] - b[1]) * (c[0] - d[0]) == (a[0] - b[0]) * (c[1] - d[1])
    m2 = (a[1] - c[1]) * (b[0] - d[0]) == (a[0] - c[0]) * (b[1] - d[1])
    m3 = (a[1] - d[1]) * (b[0] - c[0]) == (a[0] - d[0]) * (b[1] - c[1])
    return 1 if m1 or m2 or m3 else 0