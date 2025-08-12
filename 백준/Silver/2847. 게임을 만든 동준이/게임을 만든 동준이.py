cnt = 0
N = int(input())
*li, = [int(input()) for _ in range(N)]

prev = li[-1]
for i in range(N-2, -1, -1):
    now = li[i]

    if prev <= now:
        cnt += now-prev+1
        prev -= 1
    else:
        prev = now

print(cnt)
