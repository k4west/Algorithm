import sys
input = sys.stdin.readline

def dist(x0, y0, x1, y1):
    return pow(x1-x0, 2) + pow(y1-y0, 2)

def main():
    W, H, X, Y, P = map(int, input().split())
    c = 0
    for _ in range(P):
        x, y = map(int, input().split())
        if X <= x <= X+W:
            if Y <= y <= Y+H:
                c += 1
        elif X-H/2 <= x < X:
            if dist(x, y, X, Y+H/2) <= pow(H, 2)/4:
                c += 1
        elif X+W < x <= X+W+H/2:
            if dist(x, y, X+W, Y+H/2) <= pow(H, 2)/4:
                c += 1
    print(c)

if __name__ == "__main__":
    main()