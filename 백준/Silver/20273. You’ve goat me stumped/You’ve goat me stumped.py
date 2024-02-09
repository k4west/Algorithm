import sys
def area():
    l, r = map(int, sys.stdin.readline().split())
    return str(int(round(3.14 * (r * (r**2 - l**2) ** 0.5) / 4, -2)))
print("\n".join(area() for _ in range(int(input()))))