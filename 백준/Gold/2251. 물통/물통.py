from collections import deque
def bfs(a, b, c):
    q = deque([[a, b, c]])
    while q:
        liters = q.popleft()
        for i in range(3):
            if liters[i]:
                for j in range(3):
                    if i==j:
                        continue
                    if buckets[j]!=liters[j]:
                        t = min(liters[i], buckets[j]-liters[j])
                        tmp = [k for k in liters]
                        tmp[i] -= t
                        tmp[j] += t
                        if not v[tmp[0]][tmp[1]][tmp[2]]:
                            q.append(tmp)
                            v[tmp[0]][tmp[1]][tmp[2]] = 1
            elif not i:
                r[liters[2]] = 1

if __name__=="__main__":
    buckets = [*map(int, input().split())]
    C = buckets[2]
    r = [0 for _ in range(C+1)]
    v = [[[0 for _ in range(C+1)] for _ in range(buckets[1]+1)]for _ in range(buckets[0]+1)]
    v[0][0][C] = 1
    bfs(0, 0, C)
    print(*[i for i in range(C+1) if r[i]])