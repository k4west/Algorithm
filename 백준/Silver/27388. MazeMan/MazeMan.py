import sys

d = ((-1, 0), (0, 1), (1, 0), (0, -1))
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
    h = d = 0
    for i in range(m):
        if graph[0][i] != 'X':
            if f(0, i):
                h += 1

    for i in range(1, n):
        if graph[i][-1] != 'X':
            if f(i, m-1):
                h += 1

    for i in range(2, m+1):
        if graph[-1][-i] != 'X':
            if f(n-1, m-i):
                h += 1
    
    for i in range(2, n):
        if graph[-i][0] != 'X':
            if f(n-i, 0):
                h += 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                d += 1
    print(h, d)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    main()