def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def max_n(tmp):
        global ans
        for i in range(N):
            for j in range(N):
                if ans < (a:=tmp[i][j]):
                    ans = a

    def up(tmp, c):
        for i in range(N):
            p = 0
            for j in range(1, N):
                if (m:=tmp[j][i]):
                    t, tmp[j][i] = tmp[p][i], 0
                    if not t:
                        tmp[p][i] = m
                    elif m == t:
                        tmp[p][i] *= 2
                        p += 1
                    else:
                        p += 1
                        tmp[p][i] = m
        if c:
            dfs(tmp, c)
        else:
            max_n(tmp)
                
    def down(tmp, c):
        for i in range(N):
            p = -1
            for j in range(2, N+1):
                if (m:=tmp[-j][i]):
                    t, tmp[-j][i] = tmp[p][i], 0
                    if not t:
                        tmp[p][i] = m
                    elif m == t:
                        tmp[p][i] *= 2
                        p -= 1
                    else:
                        p -= 1
                        tmp[p][i] = m
        if c:
            dfs(tmp, c)
        else:
            max_n(tmp)

    def left(tmp, c):
        for i in range(N):
            p = 0
            for j in range(1, N):
                if (m:=tmp[i][j]):
                    t, tmp[i][j] = tmp[i][p], 0
                    if not t:
                        tmp[i][p] = m
                    elif m == t:
                        tmp[i][p] *= 2
                        p += 1
                    else:
                        p += 1
                        tmp[i][p] = m
        if c:
            dfs(tmp, c)
        else:
            max_n(tmp)
                
    def right(tmp, c):
        for i in range(N):
            p = -1
            for j in range(2, N+1):
                if (m:=tmp[i][-j]):
                    t, tmp[i][-j] = tmp[i][p], 0
                    if not t:
                        tmp[i][p] = m
                    elif m == t:
                        tmp[i][p] *= 2
                        p -= 1
                    else:
                        p -=1
                        tmp[i][p] = m
        if c:
            dfs(tmp, c)
        else:
            max_n(tmp)

    def dfs(mat, c):
        if not c:
            return
        for f in (up, down, left, right):
            f([row[:] for row in mat], c-1)

    dfs(matrix, 5)    
    print(ans)

if __name__ == "__main__":
    ans = 0
    main()