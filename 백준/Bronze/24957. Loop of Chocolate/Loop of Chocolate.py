pi=3.141592653589793
a = open(0)
n, r = map(int, next(a).split())
s = 4*n*pi*r**3/3
x0, y0, z0 = map(int, next(a).split())
x1, y1, z1 = x0, y0, z0
for _ in range(n-1):
    x, y, z = map(int, next(a).split())
    d = ((x-x0)**2+(y-y0)**2+(z-z0)**2)**.5
    s -= 2/3*pi*(r - d/2)**2*(2*r+d/2)
    x0, y0, z0 = x, y, z
d = ((x1-x)**2+(y1-y)**2+(z1-z)**2)**.5
s -= 2/3*pi*(r - d/2)**2*(2*r+d/2)
print(s)