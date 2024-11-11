def main():
    d = ((1, 0), (0, 1), (1, 1), (-1, 1))
    board = [*map(int, open(0).read().split())]
    t = 0
    for i in range(19):
        for j in range(19):
            if (s:=board[19*i+j]):
                for di, dj in d:
                    c = 0
                    ni, nj = i+di, j+dj
                    while 0 <= ni < 19 and nj < 19 and s == board[19*ni+nj]:
                        c += 1
                        ni, nj = ni+di, nj+dj
                    if c == 4:
                        if 0<=i-di<19 and j-dj >= 0 and s==board[19*(i-di)+j-dj]:
                            continue
                        print(s)
                        print(i+1, j+1)
                        return
    print(t)
main()