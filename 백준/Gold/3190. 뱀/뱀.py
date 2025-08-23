def turn(s, d):
    if s == "L":
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d


D = ((0, 1), (-1, 0), (0, -1), (1, 0))
N = int(input())

board = [[0]*(N) for _ in range(N)]
board[0][0] = D[0]
for _ in range(int(input())):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

turns = {int((x:=input().split())[0]): x[1] for _ in range(int(input()))}

sr = sc = r = c = t = d = 0
while True:
    t += 1
    
    dr, dc = D[d]
    nr, nc = r+dr, c+dc
    if 0 <= nr < N and 0 <= nc < N and not isinstance(board[nr][nc], tuple):
        if not board[nr][nc]:
            sdr, sdc = board[sr][sc]
            board[sr][sc] = 0
            sr, sc = sr+sdr, sc+sdc
        r, c = nr, nc

        if t in turns:
            d = turn(turns[t], d)
        board[r][c] = D[d]
    else:
        break

print(t)
