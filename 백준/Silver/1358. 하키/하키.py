import sys
input = lambda:map(int, sys.stdin.readline().split())
W, H, X, Y, P = input()
c, r = 0, H/2
X1, Y1, r2 = X+W, Y+H, pow(r, 2)
for _ in range(P):
    x, y = input()
    t = pow(Y+r-y, 2)
    if (X <= x <= X1 and Y <= y <= Y1) or pow(X-x, 2) + t <= r2 or pow(X1-x, 2) + t <= r2:
        c += 1
print(c)