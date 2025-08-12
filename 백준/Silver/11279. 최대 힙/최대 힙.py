from heapq import heappush, heappop

ans = []
hq = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x:
        heappush(hq, -x)
    elif hq:
        ans.append(-heappop(hq))
    else:
        ans.append(0)

print("\n".join(map(str, ans)))