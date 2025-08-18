from heapq import heapify, heappush, heappop


N, M = map(int, input().split())
pool = [[*map(int, input().split())] for _ in range(N)]

hq = []    # 가장자리 높이, 좌표
for i in range(1, N-1):
    hq.append((pool[i][0], i, 0))
    hq.append((pool[i][M-1], i, M-1))
for j in range(1, M-1):
    hq.append((pool[0][j], 0, j))
    hq.append((pool[N-1][j], N-1, j))
heapify(hq)

water = 0
d = ((0, 1), (0, -1), (-1, 0), (1, 0))
v = [[0]*M for _ in range(N)]
while hq:
    h, i, j = heappop(hq)
    
    for di, dj in d:
        ni, nj = i+di, j+dj
        
        # 방문 안한 내부 탐색
        if 0 < ni < N-1 and 0 < nj < M-1 and not v[ni][nj]:
            v[ni][nj] = 1
            nh = pool[ni][nj]
            
            if nh < h:
                water += h-nh
                nh = h        # 채워진 높이로 반영
            heappush(hq, (nh, ni, nj))
print(water)
