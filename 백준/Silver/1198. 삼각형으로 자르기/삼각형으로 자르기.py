def area(a, b, c):
    return abs((a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1]))/2

a = open(0)
N = int(next(a))
points = [[*map(int, i.split())] for i in a.read().split('\n')]
m = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if m < (t:=area(points[i], points[j], points[k])):
                m = t
print(m)