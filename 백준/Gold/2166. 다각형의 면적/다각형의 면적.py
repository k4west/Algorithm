import sys
input = sys.stdin.readline

def cal(x0, y0):
    global area
    for _ in range(N-1):
        x1, y1 = map(int, input().split())
        area += x0*y1 - x1*y0
        x0, y0 = x1, y1
    return x1, y1, area

def main():
    x, y = map(int, input().split())
    x1, y1, area = cal(x, y)
    area += x1*y - x*y1
    print(abs(round(area/2, 1)))

if __name__ == "__main__":
    N = int(input())
    area = 0
    main()