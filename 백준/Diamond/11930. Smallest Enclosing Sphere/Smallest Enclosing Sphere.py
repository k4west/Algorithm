def dist2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def ses(n):
    points = [[*map(int, input().split())] for _ in range(n)]

    xs, ys, zs = zip(*points)
    cx, cy, cz = map(lambda s: sum(s)/n, (xs, ys, zs))
    step = max(max(xs), -min(xs), max(ys), -min(ys), max(zs), -min(zs))
    
    for _ in range(6000):
        r2 = 0
        q = []
        
        for p in points:
            t2 = dist2((cx, cy, cz), p)
            if r2 < t2:
                r2 = t2
                q = p
        
        d = r2**.5
        dx, dy, dz = q[0]-cx, q[1]-cy, q[2]-cz
        cx += dx/d*step
        cy += dy/d*step
        cz += dz/d*step
        
        step *= 0.995
        if step < 1e-9:
            break
    
    return d


def main():
    N = int(input())
    d = ses(N)
    print(f"{d:.2f}")

    
if __name__ == "__main__":
    main()