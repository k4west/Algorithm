import sys
def f():
    N = int(sys.stdin.readline())
    li = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
    c, e = 0, 0
    for a, b in li:
        if e <= a:
            e = b
            c += 1
    print(c)
if __name__ == "__main__": f()