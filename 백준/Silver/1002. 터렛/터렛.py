import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == 0 and r2 == 0:
            print(1)
        elif r1 != r2:
            print(0)
        else:
            print(-1)
    else:
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        r = r1 + r2
        ar = abs(r1- r2)
        if d > r or d < ar:
            print(0)
        elif d < r and d != ar:
            print(2)
        else:
            print(1)