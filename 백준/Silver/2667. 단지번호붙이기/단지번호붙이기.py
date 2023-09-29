import sys
def main():
    N = int(sys.stdin.readline())
    d = ((-1,0), (1,0), (0,-1), (0,1))
    graph = []
    answer = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().rstrip()))
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '1':
                graph[i][j] = '0'
                c, q = 1, [(i, j)]
                while q:
                    y, x = q.pop(0)
                    for dy, dx in d:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == '1':
                            c += 1
                            q.append((ny, nx))
                            graph[ny][nx] = '0'
                answer.append(c)
    answer.sort()
    print(len(answer))
    print("\n".join(map(str, answer)))
if __name__=="__main__":
    main()