def check(i, j, liters):
    if buckets[j]!=liters[j]:
        t = min(liters[i], buckets[j]-liters[j])
        liters[i] -= t
        liters[j] += t
        if not v[liters[0]][liters[1]][liters[2]]:
            v[liters[0]][liters[1]][liters[2]] = 1
            return liters
    return False
    
def bfs(a, b, c):
    q = [[a, b, c]]
    while q:
        liters = q.pop()
        for i in range(3):
            if liters[i]:
                for j in range(3):
                    if i==j:
                        continue
                    if (tmp:=check(i, j, [*liters])):
                        q.append(tmp)
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