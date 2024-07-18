n, *a = open(0)
visit = [0] * 200001
c = 0
for i in a:
    idx, state = map(int, i.split())
    if visit[idx] != state:
        visit[idx] = state
    else:
        c += 1
print(c + sum(visit))