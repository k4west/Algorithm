# 거북이
ans = []
INF = float("inf")
d = ((1, 0), (0, 1), (-1, 0), (0, -1))    # 북동남서
for _ in range(int(input())):
    x = y = direction = 0   # 처음에 (0, 0), 북쪽
    max_x = max_y = min_x = min_y = 0
    for order in input():
        if order == "F":
            dy, dx = d[direction]
            x += dx
            y += dy
            if min_x > x:
                min_x = x
            if min_y > y:
                min_y = y
            if max_x < x:
                max_x = x
            if max_y < y:
                max_y = y
        elif order == "B":
            dy, dx = d[direction]
            x -= dx
            y -= dy
            if min_x > x:
                min_x = x
            if min_y > y:
                min_y = y
            if max_x < x:
                max_x = x
            if max_y < y:
                max_y = y
        elif order == "L":
            direction = (direction-1) % 4
        else:   # if order == "R":
            direction = (direction+1) % 4

    ans.append((max_x-min_x)*(max_y-min_y)) # 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이

print("\n".join(map(str, ans)))
