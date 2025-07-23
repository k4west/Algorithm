ans = []
for _ in range(4):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    if x1 < x2 or x3 < x0 or y1 < y2 or y3 < y0:
        ans.append('d')
    elif x1 == x2 or x3 == x0:
        if y3 == y0 or y1 == y2:
            ans.append('c')
        else:
            ans.append('b')
    elif y3 == y0 or y1 == y2:
        ans.append('b')
    else:
        ans.append('a')
print('\n'.join(ans))
