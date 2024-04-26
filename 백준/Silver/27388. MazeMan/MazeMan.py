import sys

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
def f(i, j):
    q = [(i, j)]
    flag = False
    while q:
        i, j = q.pop(0)
        for di, dj in d:
            if 1 <= (ni:=i+di) < n-1 and 1 <= (nj:=j+dj) < m-1 and graph[ni][nj] != 'X':
                q.append((ni, nj))
                if graph[ni][nj] == '.':
                    flag = True
                graph[ni][nj] = 'X'
    return flag

def main():
    i = s = t = 0
    j = -1
    for di, dj in d:
        while 0 <= (ni:=i+di) < n and 0 <= (nj:=j+dj) < m:
            i, j = ni, nj
            if graph[ni][nj] != 'X':
                if f(ni, nj):
                    s += 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                t += 1
    print(s, t)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    main()