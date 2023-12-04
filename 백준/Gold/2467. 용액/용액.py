N = int(input())
liq = list(map(int, input().split()))

x = float('inf')
s, e = 0, N-1
while s < e:
    t = liq[s]+liq[e]
    if t == 0:
        ans = [liq[s], liq[e]]
        break
    if t > 0:
        if x > t:
            x = t
            ans = [liq[s], liq[e]]
        e -= 1
    else:
        if x > -t:
            x = -t
            ans = [liq[s], liq[e]]
        s += 1
print(*ans, sep=' ')