from heapq import heappush, heappop

ans = []
hq = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x:
        heappush(hq, (abs(x), x))
    elif hq:
        _, m = heappop(hq)
        ans.append(m)
    else:
        ans.append(0)

print("\n".join(map(str, ans)))