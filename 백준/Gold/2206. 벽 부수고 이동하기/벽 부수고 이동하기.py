from collections import deque

def main():
    N, M = map(int, input().split())
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    ans = '-1'
    graph = [list(map(int, input())) for _ in range(N)]

    q = deque()
    q.append((0, 0, False, 1))
    graph[0][0] = 2

    while q:
        n, m, w, c = q.popleft()
        if n == N-1 and m == M-1:
            ans = c
            break
        for dx, dy in d:
            nn = n + dy
            nm = m + dx
            if not (0 <= nn < N and 0 <= nm < M):
                continue
            # 벽을 부수고 이동
            if graph[nn][nm] == 1 and not w:
                graph[nn][nm] = 2
                q.append((nn, nm, True, c+1))
            # 처음 가는 길로 이동
            elif not graph[nn][nm]:
                if not w:
                    q.append((nn, nm, w, c+1))
                    graph[nn][nm] = 2
                else:
                    q.append((nn, nm, w, c+1))
                    graph[nn][nm] = 3
            # 벽 부수기 전, (이전에 벽을 부수고 지나간) 길로 이동 
            elif graph[nn][nm] == 3 and not w:
                q.append((nn, nm, w, c+1))
                graph[nn][nm] = 2

    print(ans)

if __name__ == "__main__":
    main()