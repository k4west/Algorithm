# 9:58
d = {"1": (0, 1), "2": (0, -1), "3": (-1, 0), "4": (1, 0)}
ans = []

# 처음에 주사위에는 모든 면에 0
dice12 = [0, 0, 0, 0]  # 위, 동, 바닥, 서
dice34 = [0, 0, 0, 0]  # 위, 남, 바닥, 북

N, M, x, y, K = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

for order in input().split():
    dx, dy = d[order]
    nx, ny = x + dx, y + dy
    
    if 0 <= nx < N and 0 <= ny < M:   # 지도 내에서만 이동 가능
        if order == "1":
            dice12 = [dice12.pop()] + dice12
            dice34[0], dice34[2] = dice12[0], dice12[2]
        elif order == "2":
            dice12.append(dice12.pop(0))
            dice34[0], dice34[2] = dice12[0], dice12[2]
        elif order == "3":
            dice34.append(dice34.pop(0))
            dice12[0], dice12[2] = dice34[0], dice34[2]
        else:
            dice34 = [dice34.pop()] + dice34
            dice12[0], dice12[2] = dice34[0], dice34[2]
        
        if not arr[nx][ny]:           # 이동한 칸에 쓰여 있는 수가 0이면
            arr[nx][ny] = dice12[2]   # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        else:                                     # 0이 아닌 경우
            dice12[2] = dice34[2] = arr[nx][ny]   # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
            arr[nx][ny] = 0                       # 칸에 쓰여 있는 수는 0이 된다
        
        x, y = nx, ny
        ans.append(dice12[0])

print('\n'.join(map(str, ans)))
