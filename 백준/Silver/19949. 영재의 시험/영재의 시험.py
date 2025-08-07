def f(n, p1, p2, score):
    global ans

    if score + 10 - n < 5:
        return

    if n == 10:
        ans += score >= 5
        return

    for i in range(1, 6):
        if i == p1 and i == p2:
            continue
        f(n+1, p2, i, score+(solution[n] == i))


ans = 0
*solution, = map(int, input().split())
f(0, 0, 0, 0)
print(ans)
