from heapq import heappush, heappop

N, M = map(int, input().split())        # 손님의 수 N, 초밥의 수 M

ans = [0]*N
orders = [[] for _ in range(200001)]
for i in range(N):
    k, *A = map(int, input().split())
    for a in A:
        heappush(orders[a], i)          # 1번 손님부터 N번 손님의 순서대로

for susi in map(int, input().split()):
    if orders[susi]:                    # 목록에 있는 초밥은 무조건 먹고,
        idx = heappop(orders[susi])     # 한 번만 먹는다.
        ans[idx] += 1

print(" ".join(map(str, ans)))         # 각 손님이 먹게 되는 초밥의 개수