def solution(n):
    A = [[0]*n for _ in range(n)]
    r, c, dr, dc = 0, 0, (0,1,0,-1), (1,0,-1,0)

    i = 1
    for m in range(n-1,0,-2):
        for j in range(4):
            for _ in range(m):
                A[r][c] = i
                r, c = r + dr[j], c + dc[j]     
                i += 1
        r, c = r + 1 , c + 1
        
    if n % 2 == 1:
        A[r][c] = n**2
        
    return A