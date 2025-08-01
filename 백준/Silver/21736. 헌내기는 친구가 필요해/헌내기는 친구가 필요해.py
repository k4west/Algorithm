d = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
campus = []
people = []

for i in range(N):
    row = input()
    campus.append(list(row))
    
    for j, k in enumerate(row):
        if k == 'I':
            start = i, j
            campus[i][j] = 'X'

cnt = 0
q = [start]
while q:
    r, c = q.pop()
    for dr, dc in d:
        if 0 <= (nr := r+dr) < N and 0 <= (nc := c+dc) < M and campus[nr][nc] != 'X':
            if campus[nr][nc] == 'P':
                cnt += 1
            
            campus[nr][nc] = 'X'
            q.append((nr, nc))

print(cnt or 'TT')
