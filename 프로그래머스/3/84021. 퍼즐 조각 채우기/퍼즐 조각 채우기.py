from collections import deque

def solution(game_board, table):
    def check_piece(i, j):
        q = deque([(i, j)])
        piece = set()
        while q:
            i, j = q.popleft()
            piece.add((i, j))
            table[i][j] = 0
            for dx, dy in d:
                if (0 <= (ni := i + dx) < n and 0 <= (nj := j + dy) < n and table[ni][nj]):
                    q.append((ni, nj))
        X, Y = min(x for x, _ in piece), min(y for _, y in piece)
        return {(x - X, y - Y) for x, y in piece}

    def check_empty(i, j):
        q = deque([(i, j)])
        empty = set()
        while q:
            i, j = q.popleft()
            empty.add((i, j))
            game_board[i][j] = 1
            for dx, dy in d:
                if (0 <= (ni := i + dx) < n and 0 <= (nj := j + dy) < n and not game_board[ni][nj]):
                    q.append((ni, nj))
        X, Y = min(x for x, _ in empty), min(y for _, y in empty)
        return {(x - X, y - Y) for x, y in empty}

    def fit_piece(empty, piece):
        if empty == piece:
            return True
        X, Y = max(x for x, _ in piece), max(y for _, y in piece)
        for _ in range(3):
            if empty == (piece := {(y, X-x) for x, y in piece}):
                return True
            X, Y = Y, X
        return False

    answer = 0
    n = len(game_board)
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    pieces = {}
    for i in range(n):
        for j in range(n):
            if table[i][j]:
                piece = check_piece(i, j)
                if (p := len(piece)) in pieces:
                    pieces[p].append(piece)
                else:
                    pieces[p] = [piece]

    for i in range(n):
        for j in range(n):
            if not game_board[i][j]:
                empty = check_empty(i, j)
                if (e := len(empty)) in pieces:
                    for idx, piece in enumerate(pieces[e]):
                        if fit_piece(empty, piece):
                            pieces[e].pop(idx)
                            answer += e
                            break

    return answer