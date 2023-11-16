from heapq import heappop, heappush
def solution(n, paths, gates, summits):
    INF = float('inf')
    summits = set(summits)
    graph = {i: {} for i in range(1, n+1)}
    for s, e, w in paths:
        graph[s][e] = w
        graph[e][s] = w

    q = []
    intensities = [INF]*(n+1)
    for gate in gates:
        q.append((0, gate))
        intensities[gate] = 0
        
    while q:
        d0, n0 = heappop(q)
        if d0 > intensities[n0]:
            continue
        for n1, d1 in graph[n0].items():
            if (d:= max(d0, d1)) < intensities[n1]:
                intensities[n1] = d
                # 산봉우리 도착하면 탐색 x
                if n1 not in summits:
                    heappush(q, (d, n1))
                    
    ans = [[s, intensities[s]] for s in summits]
    ans.sort(key=lambda x: (x[1], x[0]))
    return ans[0]