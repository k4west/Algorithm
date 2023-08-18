s = set()
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    s.update({(col,row) for col in range(x1, x2) for row in range(y1, y2)})
print(len(s))