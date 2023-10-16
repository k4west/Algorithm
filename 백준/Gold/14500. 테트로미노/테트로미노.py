from sys import stdin
input = stdin.readline
ans = 0

def main():
    N, M = map(int, input().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    T = [list(map(int, input().split())) for _ in range(N)]
    m = max(map(max, T))    # 가장 큰 값
    
    def dfs(y, x, cnt, s):
        global ans

        # 남은 기회로 모두 최댓값을 탐색하는 경우의 값이 
        # 현재 정답보다 작으면 탐색의 의미가 없음
        if ans > s + m*(4-cnt):
            return
        
        if cnt == 4:        # 4칸 탐색 완료시
            ans = max(ans, s)   # 정답을 최댓값으로 업데이트
            return
        
        for dy, dx in d:    # 상, 하, 좌, 우
            ny, nx = y + dy, x + dx
            # 범위 내 방문 안 한 칸으로 탐색
            if 0 <= ny < N and 0 <= nx < M and T[ny][nx]:
                t = T[ny][nx]
                if cnt == 2:    # 테트로미노 모양 반영
                    T[ny][nx] = False       # 탐색 표시
                    dfs(y, x, cnt+1, s+t)   # 탐색한 칸 수 +1, 탐색한 칸들의 합 업데이트
                    T[ny][nx] = t       # 다른 탐색의 경우의 수에 포함하기 위해 원래 값으로 복원
                T[ny][nx] = False
                dfs(ny, nx, cnt+1, s+t)
                T[ny][nx] = t

    for row in range(N):
        for col in range(M):
            t = T[row][col]
            T[row][col] = False
            dfs(row, col, 1, t)
            T[row][col] = t

    print(ans)


if __name__ == "__main__":
    main()