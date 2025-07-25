N = int(input())
ans = sm = 0
s = e = 1
while s <= N:
    sm += e
    e += 1
    while sm > N:
        sm -= s
        s += 1
    if sm == N:
        ans += 1
print(ans)
