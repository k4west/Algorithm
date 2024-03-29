import sys


def check(board):
    for t in row_col_diag(board):
        for line in t:
            counts = [0, 0]
            for mark in line:
                if mark == "T":
                    counts[0] += 1
                    counts[1] += 1
                elif mark == "X":
                    counts[0] += 1
                elif mark == "O":
                    counts[1] += 1
            if counts[0] == 4:
                return 0
            elif counts[1] == 4:
                return 1
    for line in board:
        if "." in line:
            return 3
    return 2


def row_col_diag(board):
    for t in [
        board,
        zip(*board),
        [[board[i][i] for i in range(4)], [board[i][3 - i] for i in range(4)]],
    ]:
        yield t


results = ["X won", "O won", "Draw", "Game has not completed"]
ans = []
board = []
for idx, line in enumerate(sys.stdin.readlines(), 1):
    if idx % 5 == 1:
        continue
    board.append(line)
    if idx % 5 == 0:
        ans.append(f"Case #{idx//5}: {results[check(board)]}")
        board = []
print("\n".join(ans))
