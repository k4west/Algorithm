def main():
    a = open(0)
    N = int(next(a))
    d = ((-1,0), (1,0), (0,-1), (0,1))
    graph = [list(next(a).strip()) for _ in range(N)]
    answer = []

    def dfs(y, x, c):
        graph[y][x] = '0'
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == '1':
                c = dfs(ny, nx, c+1)
        return c

    for i in range(N):
        for j in range(N):
            if graph[i][j] == '1':
                answer.append(dfs(i, j, 1))

    answer.sort()
    print(len(answer))
    print("\n".join(map(str, answer)))

if __name__=="__main__":
    main()