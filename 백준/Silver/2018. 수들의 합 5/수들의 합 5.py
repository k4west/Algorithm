N = int(input())

cnt = sm = s = 0
for e in range(1, N+1):
    sm += e
    while sm > N:
        sm -= s
        s += 1
    if sm == N:
        cnt += 1

print(cnt)