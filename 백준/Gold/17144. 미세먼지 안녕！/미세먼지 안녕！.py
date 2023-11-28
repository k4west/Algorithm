import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
air = [(i, 0) for i, row in enumerate(graph) if row[0] == -1]

def spread(R, C):
    tmp = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            dust = graph[r][c]
            if not (d:= dust//5) or dust == -1:
                continue
            count = 0
            if 0 <= (nr:=r-1) and (nr, c) not in air:
                tmp[nr][c] += d
                count += 1
            if (nr:=r+1) < R and (nr, c) not in air:
                tmp[nr][c] += d
                count += 1
            if 0 <= (nc:=c-1) and (r, nc) not in air:
                tmp[r][nc] += d
                count += 1
            if (nc:=c+1) < C:
                tmp[r][nc] += d
                count += 1
            graph[r][c] -= d*count

    for r in range(R):
        for c in range(C):
            graph[r][c] += tmp[r][c]
    return

def rotate(R):
    r0, r1 = air[0][0], air[1][0]
    graph[r0][0] = 0
    graph[r1][0] = 0
    t0, t1 = r0, 1
    while t0:
        graph[t0].insert(0, graph[t0-1].pop(0))
        graph[r0-t0].append(graph[r0-t0+1].pop())
        t0 -= 1
    while r1 + t1 < R:
        graph[r1+t1-1].insert(0, graph[r1+t1].pop(0))
        graph[R-t1].append(graph[R-t1-1].pop())
        t1 += 1
    graph[air[0][0]][0] = -1
    graph[air[1][0]][0] = -1


for _ in range(T):
    spread(R, C)
    rotate(R)

s = sum(sum(graph, []))
print(s+2)