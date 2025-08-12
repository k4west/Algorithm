N = int(input())
*limits, = map(int, input().split())
M = int(input())
*weights, = map(int, input().split())

limits.sort(reverse=True)
weights.sort(reverse=True)

cost = -1

if limits[0] >= weights[0]:
    cranes = [0]*N

    for w in weights:
        idx = 0
        cnt = M

        for i in range(N):
            # 실을 수 있는 무게 and 적게 사용한 크레인
            if w <= limits[i] and cnt > cranes[i]:
                idx = i
                cnt = cranes[i]

        cranes[idx] += 1

    for tmp in cranes:
        if cost < tmp:
            cost = tmp

print(cost)