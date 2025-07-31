def main():
    d = ((1, 0), (0, 1), (1, 1), (-1, 1))
    graph = [[*map(int, input().split())] for _ in range(19)]
    for i in range(19):
        for j in range(19):
            if t := graph[i][j]:
                for di, dj in d:
                    if 0 <= i-di < 19 and 0 <= j-dj < 19 and graph[i-di][j-dj] == t:
                        continue
                    cnt = 1
                    ni, nj = i, j
                    while 0 <= (ni := ni+di) < 19 and 0 <= (nj := nj+dj) < 19 and graph[ni][nj] == t:
                        cnt += 1
                        if cnt > 5:
                            break
                    if cnt == 5:
                        print(t)
                        print(i+1, j+1)
                        return
    print(0)


main()