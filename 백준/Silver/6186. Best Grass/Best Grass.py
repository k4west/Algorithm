d = ((0,1),(1,0))
rc, *a = open(0)
r, c = map(int, rc.split())
a = [*map(list,a),['']*(c+1)]
count = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == '#':
            count += 1
            a[i][j] = '.'
            for di, dj in d:
                a[i+di][j+dj] = '.'
print(count)