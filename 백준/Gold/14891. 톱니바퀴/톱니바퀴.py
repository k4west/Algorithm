def rotate(n, wise):
    if wise == 1:
        t = gears[n].pop()
        gears[n] = [t] + gears[n]
    
    else:
        gears[n].append(gears[n].pop(0))


def bfs(info):
    li = [info]
    
    q, nq = [info], []
    visited = [0]*(5)
    visited[info[0]] = 1
    
    while q or nq:
        if not q:
            q, nq = nq, []
        
        cn, cw = q.pop()
        for move, ci, ni in d:
            nn = cn + move
            if 0 < nn < 5 and not visited[nn] and gears[cn][ci] != gears[nn][ni]:
                visited[nn] = 1

                nw = cw * -1
                nq.append((nn, nw))
                li.append((nn, nw))
    
    for n, w in li:
        rotate(n, w)


d = ((-1, 6, 2), (1, 2, 6))
gears = [[]] + [[*map(int, input())] for _ in range(4)]
for _ in range(int(input())):
    bfs(tuple(map(int, input().split())))

print(sum(g[0]*(2*g[0])**i for i, g in enumerate(gears[1:])))