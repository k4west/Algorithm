def main():
    d = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    board = [s for s in open(0)]
    for i in range(10):
        for j in range(10):
            if board[i][j] == "X":
                for di, dj in d:
                    cnt, flag, ti, tj = 1, True, i, j
                    while 0 <= (ni := ti + di) < 10 and 0 <= (nj := tj + dj) < 10:
                        if board[ni][nj] == "X": cnt += 1
                        elif board[ni][nj] == "." and flag: cnt += 1; flag = False
                        else: break
                        ti, tj = ni, nj
                    if cnt == 5 or (flag and cnt == 4 and 0<=(ni:=i-di)<10 and 0<=(nj:=j-dj)<10 and board[ni][nj]=='.'): print(1); exit(0)
    print(0)
main()