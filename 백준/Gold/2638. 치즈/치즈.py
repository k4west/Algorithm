import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    margin = [[-1]*(M+2)]
    graph = [[-1]+list(map(int, input().split()))+[-1] for _ in range(N)]
    graph = margin + graph + margin

    q, nq, t = [(1, 1)], [], 0
    while q or nq:
        if not q:
            q, nq = nq, []
            t += 1
        r, c = q.pop()
        for dr, dc in d:
            if graph[(nr:=r+dr)][(nc:=c+dc)] > 0:
                graph[nr][nc] += 1
                if graph[nr][nc] > 2:
                    graph[nr][nc] = -1
                    nq.append((nr, nc))
            if not graph[nr][nc]:
                graph[nr][nc] = -1
                q.append((nr, nc))
    print(t)

if __name__ == "__main__":
    main()