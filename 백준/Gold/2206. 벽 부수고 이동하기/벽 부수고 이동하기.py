from collections import deque

def main():
    N, M = map(int, input().split())
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    ans = '-1'
    graph = [list(map(int, input())) for _ in range(N)]
    v = [[[0, 0] for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append((0, 0, 0))
    v[0][0][0] = 1

    while q:
        n, m, w = q.popleft()
        if n == N-1 and m == M-1:
            ans = v[n][m][w]
            break
        for dx, dy in d:
            nn = n + dy
            nm = m + dx
            if not (0 <= nn < N and 0 <= nm < M):
                continue
            # 벽을 부수고 이동
            if graph[nn][nm] and not w:
                v[nn][nm][1] = v[n][m][0] + 1
                q.append((nn, nm, 1))
            # 벽을 부술 수 있는 기회에 따른 방문하지 않은 길로 이동
            elif not graph[nn][nm] and not v[nn][nm][w]:
                v[nn][nm][w] = v[n][m][w] + 1
                q.append((nn, nm, w))
    print(ans)

if __name__ == "__main__":
    main()