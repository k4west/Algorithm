# 도로 정비
# 도시가 수도에 방문 -> 몇 개의 도시 방문?(최소)

E = 1
n, m = map(int, input().split())  # n: 도시 수, m 도로 수
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split()) # 연결된 두 도시
    graph[s].append(e)
    graph[e].append(s)

ans = []
# 한 도로가 정비될 때마다 각 도시별로 수도를 방문하는 데 최소 방문 도시
for _ in range(int(input())):  # 정비할 도로 수
    s, e = map(int, input().split()) # 연결할 두 도시
    graph[s].append(e)
    graph[e].append(s)
    
    li = [-1]*n
    li[0] = 0
    cnt = 0
    q, nq = [1], []
    while q:
        cnt += 1
        for cur in q:
            for nxt in graph[cur]:
                if li[nxt-1] != -1:
                    continue
                li[nxt-1] = cnt
                nq.append(nxt)
        q, nq = nq, []
    ans.append(li)

print('\n'.join((' '.join(map(str, i)) for i in ans)))
