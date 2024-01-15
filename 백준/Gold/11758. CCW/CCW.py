import sys

def main():
    input = lambda: map(int, sys.stdin.readline().split())
    (x1, y1), (x2, y2), (x3, y3) = input(), input(), input()
    if z := (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1):
        return print([-1, 1][z > 0])
    return print(0)

if __name__ == "__main__":
    main()