L = int(input())
cake = [0]*(L+1)
m1 = m2 = i1 = i2 = 0

for idx in range(1, int(input())+1):
    s, e = map(int, input().split())
    expected, cnt = e-s, 0
    
    for i in range(s, e+1):
        if not cake[i]:
            cake[i] = idx
            cnt += 1

    if m1 < expected:
        m1 = expected
        i1 = idx

    if m2 < cnt:
        m2 = cnt
        i2 = idx

print(i1)
print(i2)
