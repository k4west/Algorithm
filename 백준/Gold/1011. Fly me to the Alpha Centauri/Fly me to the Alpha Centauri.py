t = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = y-x
    for i in range(int(d**.5), 65537):
        if d <= (s:=i*(i+1)):
            t.append(2*i-(s-i>=d))
            break
print('\n'.join(map(str, t)))