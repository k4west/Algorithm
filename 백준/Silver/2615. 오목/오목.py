d = (19, 1, 20, -18)
*graph, = map(int, open(0).read().split())
flag = True

for i in range(361):
    if not (t := graph[i]):
        continue

    for di in d:
        if i % 19 >= (i - di) % 19 and 0 <= i - di < 361 and graph[i - di] == t:
            continue

        cnt, ni = 1, i
        while i % 19 <= (ni + di) % 19 and 0 <= (ni := ni + di) < 361 and graph[ni] == t:
            cnt += 1
            if cnt > 5:
                break

        if cnt == 5:
            print(t)
            print(i // 19 + 1, i % 19 + 1)
            flag = False

        if not flag:
            break
    if not flag:
        break
if flag:
    print(0)
