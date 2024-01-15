def solution(board, h, w):
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    H, W = len(board), len(board[0])
    color = board[h][w]
    
    answer = 0
    for dh, dw in d:
        if 0 <= (nh:=h+dh) < H and 0 <= (nw:=w+dw) < W:
            if board[nh][nw] == color:
                answer += 1
    return answer