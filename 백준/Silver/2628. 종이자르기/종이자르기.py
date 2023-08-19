width, height = map(int, input().split())
w, h = [0], [0]
for _ in range(int(input())):
    c, n = map(int, input().split())
    if c: 
        w.append(n)
    else:
        h.append(n)
w.sort()
h.sort()
w.append(width)
h.append(height)
a = max([w[i+1]-w[i] for i in range(len(w)-1)])
b = max([h[i+1]-h[i] for i in range(len(h)-1)])
print(a*b)