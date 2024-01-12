from heapq import heappop, heappush
def solution(gems):
    n, g = len(set(gems)), len(gems)
    visited, heap = {}, []
    for e, gem in enumerate(gems, 1):
        visited[gem] = e
        if len(visited) == n:
            s = g
            for idx in visited.values():
                if s > idx: s = idx
            heappush(heap, (e-s, [s, e]))
            print(s)
            del visited[gems[s-1]]
    return heappop(heap)[1]