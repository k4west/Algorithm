# 문제 읽고, 입력 받기(11분)
# 구상 및 초기값 세팅(7분)
# 구현(17분)

from collections import deque


D = ((0, 1), (-1, 0), (0, -1), (1, 0)) # 우상좌하

# 초기
t = 0
snake = deque([(0, 0)])   # 시작할때 뱀은 맨위 맨좌측에 위치하고
# length = 1  # 뱀의 길이는 1   # 필요없는 변수라서 주석 처리
d = 0 # 뱀은 처음에 오른쪽을 향한다

# 입력
## 보드
N = int(input())   # 보드의 크기(2 ≤ N ≤ 100)
board = [[0]*(N) for _ in range(N)]   # 보드의 상하좌우 끝에 벽이 있다.
board[0][0] = 1

## 사과
K = int(input())   # 사과의 개수(0 ≤ K ≤ 100)
for _ in range(K):
    r, c = map(int, input().split())  # 사과의 위치는 모두 다르며, (1행 1열) 에는 사과가 없다.
    board[r-1][c-1] = 2


## 뱀의 방향 변환 정보
L = int(input())    # 뱀의 방향 변환 횟수(1 ≤ L ≤ 100)
turns = {}          ## 딕셔너리가 아닌 리스트라면 10001개; 상관 없나?
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C   # X는 10,000 이하의 양의 정수; X가 증가하는 순으로 주어진다.


def turn(s, d):   # 왼쪽('L') 또는 오른쪽('D')로 90도 방향을 회전
    if s == "L":
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d

# 규칙
while True:
    r, c = snake[-1]
    t += 1
    
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    dr, dc = D[d]
    nr, nc = r+dr, c+dc   ## 오타 있었음
    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1:
        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if not board[nr][nc]:   # 만약 이동한 칸에 사과가 없다면, 
            er, ec = snake.popleft()
            board[er][ec] = 0   # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        board[nr][nc] = 1
        snake.append((nr, nc))  ## 추가 안하고 있었음
        
        if t in turns:# 게임 시작 시간으로부터 X초가 끝난 뒤에 방향 전환
            d = turn(turns[t], d)   ## 함수만 만들어 두고 이 코드를 작성 안했음

    else:   # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
        break


print(t)  # 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산
