from collections import deque
def main():
    def dfs(i, j, w, h):
        q = deque([(i, j)])
        while q:
            i, j = q.popleft()
            for di, dj in d:
                if 0 <= (ni:=i+di) < h and 0 <= (nj:=j+dj)< w and graph[ni][nj] == 1:
                    graph[ni][nj] = 0
                    q.append((ni, nj))

    *a, = map(int, open(0).read().split())
    idx = 0
    while True:
        w, h = a[idx:idx+2]
        if w == 0: break
        idx += 2
        graph = [a[idx+i*w:idx+i*w+w] for i in range(h)]
        idx += w*h
        c = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j]:
                    c += 1
                    graph[i][j] = 0
                    dfs(i, j, w, h)
        t.append(c)
    print("\n".join(map(str, t)))

t = []
d = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
main()