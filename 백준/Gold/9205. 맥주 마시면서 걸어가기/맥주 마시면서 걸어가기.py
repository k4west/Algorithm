def get_dist(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])


def bfs():
    q, nq = [0], []
    visited[0] = 1

    while q or nq:
        if not q:
            q, nq = nq, []

        c = q.pop()
        for n in graph[c]:
            if n == N+1:
                return True

            if not visited[n]:
                visited[n] = 1
                nq.append(n)
    return False


ans = []
m = 1001

for _ in range(int(input())):
    N = int(input())
    pos = [[*map(int, input().split())] for _ in range(N+2)]

    # 이동 가능성 확인
    graph = [[] for _ in range(N+2)]
    visited = [0] * (N+2)
    for i in range(N+1):
        for j in range(i+1, N+2):
            if get_dist(pos[i], pos[j]) < m:
                graph[i].append(j)
                graph[j].append(i)

    ans.append("happy" if graph[0] and graph[-1] and bfs() else "sad")
print('\n'.join(ans))