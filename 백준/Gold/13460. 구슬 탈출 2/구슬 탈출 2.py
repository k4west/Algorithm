def move(direction, p):
    r0, c0 = p
    r, c = r0, c0
    dr, dc = d[direction]
    while 1 <= (nr := r + dr) < N - 1 and 1 <= (nc := c + dc) < M - 1:
        if (b := tmp_board[nr][nc]) != ".":
            if b == "O":
                tmp_board[r0][c0] = "."
                return -1
            break
        r, c = nr, nc
    if r != r0 or c != c0:
        tmp_board[r][c], tmp_board[r0][c0] = tmp_board[r0][c0], "."
    return (r, c)


if __name__ == "__main__":
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline
    N, M = map(int, input().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상, 하, 좌, 우
    board = []
    marbles = {}  # 구슬의 위치를 저장한 딕셔너리; 색상: (행, 열)
    for i in range(N):
        row = list(input().rstrip())
        for j, x in enumerate(row):
            if x in "RB":
                marbles[x] = (i, j)
        board.append(row)

    flag = False
    heap = [(0, marbles["R"], marbles["B"], board)]
    while heap:
        count, red, blue, t_board = heappop(heap)
        # print(count, red, blue)
        count += 1
        for i in range(4):
            tmp_board = [row[::] for row in t_board]
            if not i % 2:
                if red[i // 2] < blue[i // 2]:
                    n_red = move(i, red)
                    n_blue = move(i, blue)
                else:
                    n_blue = move(i, blue)
                    n_red = move(i, red)
            else:
                if red[i // 2] < blue[i // 2]:
                    n_blue = move(i, blue)
                    n_red = move(i, red)
                else:
                    n_red = move(i, red)
                    n_blue = move(i, blue)

            if count > 10:
                print(-1)
                flag = True
                break
            elif n_red == -1 and n_blue != -1:
                print(count)
                flag = True
                break
            if (n_red == red and n_blue == blue) or n_blue == -1:
                continue
            heappush(heap, (count, n_red, n_blue, tmp_board))
        if flag:
            break
    if not flag:
        print(-1)