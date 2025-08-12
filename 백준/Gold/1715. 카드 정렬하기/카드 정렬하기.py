from heapq import heappop, heappush, heapify

cnt = 0
N = int(input())
sizes = [int(input()) for _ in range(N)]
heapify(sizes)

for _ in range(N-1):
    size = heappop(sizes) + heappop(sizes)
    cnt += size
    heappush(sizes, size)

print(cnt)