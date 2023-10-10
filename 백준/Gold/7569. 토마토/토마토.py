import sys
from collections import deque

def ripen(H, N, M, tomato):
    ripen = deque()
    d = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
    
    # 초기 익은 토마토를 큐에 추가
    for i in range(H):
        for col in range(N):
            for row in range(M):
                if tomato[i][col][row] == 1:
                    ripen.append((i, col, row))
    
    days = 1  # 일 수 초기화
    
    # BFS를 사용하여 토마토 익는 과정 시뮬레이션
    while ripen:
        h, n, m = ripen.popleft()
        c = tomato[h][n][m]
        for dm, dn, dh in d:
            nh, nn, nm = h + dh, n + dn, m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
                if not tomato[nh][nn][nm]:
                    ripen.append((nh, nn, nm))
                    tomato[nh][nn][nm] = c + 1
                    days = max(days, c + 1)
    
    return days

def count_days(H, N, M, tomato):
    for i in range(H):
        for col in range(N):
            for row in range(M):
                if tomato[i][col][row] == 0:
                    return False  # 아직 익지 않은 토마토가 있으면 False 반환
    return True  # 모든 토마토가 익었으면 True 반환

def main():
    M, N, H = map(int, sys.stdin.readline().split())
    tomato = [[[0] * M for _ in range(N)] for _ in range(H)]
    
    # 토마토 상태 입력
    for i in range(H):
        for col in range(N):
            tomato[i][col] = list(map(int, sys.stdin.readline().split()))
    
    # 모든 토마토가 익었는지 확인
    if count_days(H, N, M, tomato):
        print(0)
    else:
        days = ripen(H, N, M, tomato)
        if count_days(H, N, M, tomato):
            print(days - 1)
        else:
            print(-1)

if __name__ == "__main__":
    main()