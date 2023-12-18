
def solution(land):
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n, m = len(land), len(land[0])
    oil = [0]*m

    def find(i, j):
        q, c = [(i, j)], 1
        v = {j}
        while q:
            x, y = q.pop(0)
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny]:
                    land[nx][ny] = 0
                    q.append((nx, ny))
                    v.add(ny)
                    c += 1
        for i in v:
            oil[i] += c
    
    for i in range(n):
        for j in range(m):
            if land[i][j]:
                land[i][j] = 0
                find(i, j)
                
    return max(oil)