N = int(input())
x = int(input())

td = [[[] for _ in range(N)] for _ in range(N)]
M = (N - 1)//2
o = [M,M]
num = 1
td[M][M] = num
for i in range(1, N, 2):
    o[0] -= 1
    o[1] -= 1
    for d in ((0,1),(1,0),(0,-1),(-1,0)):
        dx, dy = d[0], d[1]
        for _ in range(i+1):
            o[0] += dx
            o[1] += dy
            num += 1
            td[o[0]][o[1]] = num
for r in td:
    print(*r)

for row in range(N):
    for col in range(N):
        if td[row][col] == x:
            print(*(row + 1, col + 1))
            exit()