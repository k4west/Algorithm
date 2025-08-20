def dist(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**.5


def ses(n):
    points = [[*map(float, input().split())] for _ in range(n)]

    xs, ys, zs = zip(*points)
    cx, cy, cz = map(lambda s: sum(s) / n, (xs, ys, zs))
    s = 0
    scale = 1e-16

    for _ in range(10000):
        ns = nx = ny = nz = w = 0

        for p in points:
            d = dist((cx, cy, cz), p) + scale

            ns += d
            nx += p[0]/d
            ny += p[1]/d
            nz += p[2]/d
            w += 1/d
        nx /= w
        ny /= w
        nz /= w

        cx, cy, cz, s = nx, ny, nz, ns

    return s


def main():
    d = ses(3)
    print(f"{d:.6f}")


if __name__ == "__main__":
    main()