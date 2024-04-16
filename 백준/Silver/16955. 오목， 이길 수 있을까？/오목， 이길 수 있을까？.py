def main():
    d = (-11, -10, -9, -1, 1, 9, 10, 11)
    board = "".join(s.rstrip() for s in open(0))
    for i in range(100):
        if board[i] == "X":
            for di in d:
                cnt, flag, ti, ni = 1, True, i, i+di
                while 0 <= ni < 100 and abs(ti//10 - ni//10) < 2 and abs(ti%10 - ni%10) < 2:
                    if board[ni] == "X": cnt += 1
                    elif board[ni] == "." and flag: cnt += 1; flag = False
                    else: break
                    ti, ni = ni, ni+di
                if cnt == 5 or (flag and cnt == 4 and 0<=(ni:=i-di)<10 and board[ni]=='.'): print(1); exit(0)
    print(0)
main()