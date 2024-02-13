def solution(maps):
    answer = 1
    n, m = len(maps), len(maps[0])
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q, nq = [(0, 0)], []
    maps[0][0] = 0
    while q:
        for i, j in q:
            if i == n-1 and j == m-1:
                return answer
            for di, dj in d:
                if 0 <= (ni := i + di) < n and 0 <= (nj := j + dj) < m and maps[ni][nj]:
                    maps[ni][nj] = 0
                    nq.append((ni, nj))
        q, nq = nq, []
        answer += 1
    return -1