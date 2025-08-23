# 7:05
# ~ 7:12 문제 읽기
# ~ 7:22 입력 받고 구상하기
# ~ 7:51 구현 & 디버깅

# 스티커
# 스티커의 각 칸은 상하좌우로 모두 연결되어 있다 (대각선 연결 x)
# 불필요한 행이나 열이 존재하지 않는다.

# 붙이기
# 먼저 받았던 것부터 차례대로 격자에 맞춰서 붙이려고 한다.

# 방법
# 1. 스티커를 회전시키지 않고 모눈종이에서 떼어낸다.
# 2. 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 
#    가장 위 -> 가장 왼쪽
# 3. 선택한 위치에 스티커를 붙인다. 
#    만약 스티커를 붙일 수 있는 위치가 전혀 없어서 스티커를 붙이지 못했다면, 
#    스티커를 시계 방향으로 90도 회전한 뒤 2번 과정을 반복한다.
# 4. 위의 과정을 네 번 반복해서 
#    스티커를 0도, 90도, 180도, 270도 회전시켜 봤음에도
#    스티커를 붙이지 못했다면 해당 스티커를 붙이지 않고 버린다.

def turn(n, m, arr):  # 시계 방향으로 90도 회전
    return [[arr[r][c] for r in range(n-1, -1, -1)] for c in range(m)]


def attach(sr, sc, n, m, arr):  # 선택한 위치에 스티커를 붙인다.
    for r in range(n):
        for c in range(m):
            if arr[r][c]:
                laptop[sr+r][sc+c] = 1
    return True


def find(n, m, arr):
    for sr in range(N-n+1):
        for sc in range(M-m+1):
            r_cnt = 0
            flag = True
            for r in range(n):
                for c in range(m):
                    if arr[r][c] and laptop[sr+r][sc+c]:
                        flag = False
                        break
                else:
                    r_cnt += 1
                if not flag:
                    break
            if r_cnt == n:
                return attach(sr, sc, n, m, arr)
    return False


def sol(n, m):
    skicker = [[*map(int, input().split())] for _ in range(R)]
    for _ in range(4):
        if find(n, m, skicker):
            break
        skicker = turn(n, m, skicker)
        n, m = m, n
    
# 입력
N, M, K = map(int, input().split())   # 세로, 가로, 스티거 개수(1 ~ 40, 40, 100)
laptop = [[0]*M for _ in range(N)]
# L = max(N, M)

# 0: 스티커가 붙지 않은 칸
# 1: 스티커가 붙은 칸
for _ in range(K):
    R, C = map(int, input().split())
    
    # if max(R, C) > L:
    #     for _ in range(R):
    #         input()
    #     continue
    sol(R, C)

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += laptop[i][j]
print(cnt)