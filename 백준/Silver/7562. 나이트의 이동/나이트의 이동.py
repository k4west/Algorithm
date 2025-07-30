def bfs():
    # 시작 == 도착
    if sr == er and sc == ec:
        return 0
    
    # 초기화
    cnt = 0
    graph[sr][sc] = 1
    q, nq = [(sr, sc)], []
    
    while q or nq:
        if not q:            # 다음 탐색할 목록
            q, nq = nq, []
            cnt += 1         # 너비우선탐색의 step = 이동 횟수
        
        r, c = q.pop(0)
        for dr, dc in d:    # 가능한 방향 탐색
            nr = r + dr
            nc = c + dc
            
            if nr == er and nc == ec:    # 도착
                return cnt + 1
            
            if 0 <= nr < l and 0 <= nc < l and not graph[nr][nc]:
                graph[nr][nc] = 1        # 방문 표시
                nq.append((nr, nc))      # 다음 탐색 목록에 추가


ans = []
d = ((-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2))
for _ in range(int(input())):
    l = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    
    graph = [[0]*l for _ in range(l)]
    ans.append(bfs())
print('\n'.join(map(str, ans)))
