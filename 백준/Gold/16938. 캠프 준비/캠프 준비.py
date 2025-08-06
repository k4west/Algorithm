def f(i, total, min_l, max_l):
    global ans

    if total > R:
        return

    if i == N:
        if L <= total <= R and max_l - min_l >= X:
            ans += 1
        return

    f(i+1, total, min_l, max_l)
    j = li[i]
    if not min_l or min_l > j:
        min_l = j
    if max_l < j:
        max_l = j
    f(i+1, total+j, min_l, max_l)


ans = 0
N, L, R, X = map(int, input().split())
*li, = map(int, input().split())
visited = [0]*N
f(0, 0, 0, 0)
print(ans)
