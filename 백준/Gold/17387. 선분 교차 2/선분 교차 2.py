import sys

input = lambda: map(int, sys.stdin.readline().split())
INF = float("inf")


def ccw(a, b, c):
    if z := (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (
        a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    ):
        return [-1, 1][z > 0]
    return z


x1, y1, x2, y2 = input()
x3, y3, x4, y4 = input()


if (u1 := max(min(x3, x4), min(x1, x2))) > (u2 := min(max(x1, x2), max(x3, x4))):
    print(0)
elif max(min(y3, y4), min(y1, y2)) > min(max(y1, y2), max(y3, y4)):
    print(0)
else:
    if (
        ccw((x1, y1), (x2, y2), (x3, y3)) * ccw((x1, y1), (x2, y2), (x4, y4)) <= 0
        and ccw((x3, y3), (x4, y4), (x1, y1)) * ccw((x3, y3), (x4, y4), (x2, y2)) <= 0
    ):
        print(1)
    else:
        print(0)