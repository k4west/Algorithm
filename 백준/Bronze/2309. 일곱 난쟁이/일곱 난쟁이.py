def f(n, i, hs, tmp):
    global ans

    if n+9-i < 7 or ans or hs > 100:
        return

    if n == 7:
        if hs == 100:
            ans = tmp
        return

    f(n, i+1, hs, tmp)
    f(n+1, i+1, hs+li[i], tmp+[li[i]])


ans = []
*li, = [int(input()) for _ in range(9)]
li.sort()
f(0, 0, 0, [])
print(*ans, sep='\n')
