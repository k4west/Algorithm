D = ((1, 2, 3, 4), (0, 2, 4, 5), (0, 1, 3, 5), (0, 2, 4, 5), (0, 1, 3, 5), (1, 2, 3, 4))
UD = (5, 3, 4, 1, 2, 0)

ans = 0
N = int(input())
dice = [[*map(int, input().split())] for _ in range(N)]

for bottom_idx in range(6):  # 1번 주사위는 마음대로 놓을 수 있다. -> 모두 다
    up = UD[bottom_idx]  # 윗면 인덱스
    u = dice[0][up]
    m = 0
    for k in D[up]:
        if m < dice[0][k]:
            m = dice[0][k]

    sm = m
    for li in dice[1:]:
        for j in range(6):
            if li[j] == u:
                break
        j = UD[j]
        u = li[j]

        m = 0
        for k in D[j]:  # 옆으로 90도, 180도, 또는 270도 돌릴 수 있다.
            if m < li[k]:
                m = li[k]
        sm += m

    if ans < sm:
        ans = sm

print(ans)  # 한 옆면의 숫자의 합이 가장 큰 값을 출력
