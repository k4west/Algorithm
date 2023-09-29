import sys
N, M = map(int, sys.stdin.readline().split())
d = ((-1,0), (1,0), (0,-1), (0,1))
maze= []
for _ in range(N):
    maze.append(list(sys.stdin.readline().rstrip()))
q = [[(0,0)]]
v = {(0,0)}
def f(c=1):
    while q != [[]]:
        c += 1
        li = q.pop(0)
        tmp = []
        for y, x in li:
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < M:
                    new = (ny, nx)
                    if new == (N-1, M-1):
                        return c
                    if maze[ny][nx] == '1' and new not in tmp:
                        if new not in v:
                            tmp.append(new)
                        v.add(new)
        q.append(tmp)
print(f())