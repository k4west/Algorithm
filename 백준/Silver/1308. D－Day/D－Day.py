import sys


def yun(n):
    return int((n % 4 == 0 and n % 25 != 0) or n % 400 == 0)


m_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def count_days(y, m, d):
    days = 365 * (y - 1) + sum(m_days[: m - 1]) + d
    for i in range(y):
        days += yun(i)
    if m > 2 and yun(y):
        days += 1
    return days


input = lambda: map(int, sys.stdin.readline().split())
y0, m0, d0 = input()
y1, m1, d1 = input()

if count_days(y1 - 1000, m1, d1) >= (t := count_days(y0, m0, d0)):
    print("gg")
else:
    print(f"D{t - count_days(y1, m1, d1)}")