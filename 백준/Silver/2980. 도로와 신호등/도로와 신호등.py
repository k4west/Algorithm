N, L = map(int, input().split())
street = [0]*(L+1)

for _ in range(N):
    D, R, G = map(int, input().split())
    street[D] = (R, G)

s = 0
for i in range(L):
    s += 1
    if street[i+1]:
        r, g = street[i+1]
        t = s % (r+g)
        if t < r:
            s += r - t
print(s)