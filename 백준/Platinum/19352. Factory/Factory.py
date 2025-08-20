def dist(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5


def ses(n):
    points = [[*map(float, input().split())] for _ in range(n)]

    xs, ys = zip(*points)
    cx, cy = map(lambda s: sum(s) / n, (xs, ys))
    s = 0
    scale = 1e-16

    for _ in range(10000):
        ns = nx = ny = w = 0

        for p in points:
            d = dist((cx, cy), p) + scale

            ns += d
            nx += p[0]/d
            ny += p[1]/d
            w += 1/d
        nx /= w
        ny /= w

        cx, cy, s = nx, ny, ns

    return cx, cy


def main():
    ans = []
    for _ in range(int(input())):
        i, j = ses(int(input()))
        ans.append(f"{i:.6f} {j:.6f}")
    print('\n'.join(ans))


if __name__ == "__main__":
    main()
