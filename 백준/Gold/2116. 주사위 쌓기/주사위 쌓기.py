D = ((1, 2, 3, 4), (0, 2, 4, 5), (0, 1, 3, 5), (0, 2, 4, 5), (0, 1, 3, 5), (1, 2, 3, 4))
UD = (5, 3, 4, 1, 2, 0)


def find_idx(n, li):     # 마주보는 면의 숫자가 같음
    for j in range(6):
        if li[j] == n:
            return UD[j]    # 마주 볼 면의 반대편(다음 윗면)의 인덱스 반환


def get_max(idx, li):   # 어느 한 면의 숫자의 합이 최대가 되도록
    m = 0
    for j in D[idx]:    # 옆으로 90도, 180도, 또는 270도 돌릴 수 있다.
        if m < li[j]:
            m = li[j]
    return m


def bf(u, m):  # 처음 정하는 방법 -> 모두 다 해보자
    # u, m: 윗면 숫자, 옆면 큰 값
    global ans

    sm = m
    for li in dice[1:]:
        j = find_idx(u, li)
        u, m = li[j], get_max(j, li)
        sm += m

    if ans < sm:
        ans = sm


ans = 0
N = int(input())
dice = [[*map(int, input().split())] for _ in range(N)]

for bottom_idx in range(6):   # 1번 주사위는 마음대로 놓을 수 있다. -> 모두 다
    up = UD[bottom_idx]       # 윗면 인덱스
    bf(dice[0][up], get_max(up, dice[0]))   # 윗면 숫자, 옆면 큰 값

print(ans)     # 한 옆면의 숫자의 합이 가장 큰 값을 출력
