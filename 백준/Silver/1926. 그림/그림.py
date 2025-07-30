def dfs(r, c):
    stack = []
    cnt = 1
    while True:
        # 연결된 그림 넓이 구하기
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and paint[nr][nc]:
                paint[nr][nc] = 0
                stack.append((r, c))
                r, c = nr, nc
                cnt += 1
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                return cnt


d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
paint = [[*map(int, input().split())] for _ in range(N)]
A = []
for r in range(N):
    for c in range(M):
        # 그림 찾기
        if paint[r][c]:
            paint[r][c] = 0
            A.append(dfs(r, c))
print(len(A))
print(max(A) if A else 0)
