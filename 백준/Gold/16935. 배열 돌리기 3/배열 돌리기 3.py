def turn_arr(op):
    if op == "1":       # 상하
        return arr[::-1]

    elif op == "2":     # 좌우
        return [row[::-1] for row in arr]

    elif op == "3":     # 오른쪽 90도
        return [[arr[j][i] for j in range(N-1, -1, -1)] for i in range(M)]

    elif op == "4":     # 왼쪽 90도
        return [[arr[j][i] for j in range(N)] for i in range(M-1, -1, -1)]

    elif op == "5":     # 4등분; 시계 방향
        n, m = N//2, M//2
        return [[arr[i+n][j] for j in range(m)] + [arr[i][j] for j in range(m)] for i in range(n)] + [[arr[i+n][j+m] for j in range(m)] + [arr[i][j+m] for j in range(m)] for i in range(n)]

    elif op == "6":     # 4등분; 반시계 방향
        n, m = N // 2, M // 2
        return [[arr[i][j+m] for j in range(m)] + [arr[i+n][j+m] for j in range(m)] for i in range(n)] + [[arr[i][j] for j in range(m)] + [arr[i+n][j] for j in range(m)] for i in range(n)]


N, M, R = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

for r in input().split():
    arr = turn_arr(r)
    if r == "3" or r == "4":
        N, M = M, N

print("\n".join(' '.join(map(str, row)) for row in arr))
