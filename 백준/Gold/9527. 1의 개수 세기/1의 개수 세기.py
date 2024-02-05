import sys


def ones(n, cnt):
    if n <= 1:
        return n

    t, i = n, 0
    while True:
        cnt = (cnt << 1) + (2**i)
        i += 1
        t = t >> 1
        if t <= 1:
            break
    c = n - (2**i) + 1

    return cnt + c + ones(c - 1, 0)


A, B = map(int, sys.stdin.readline().split())
print(ones(B, 0) - ones(A - 1, 0))