import sys

def check(board):
    a, b, c = [board, zip(*board), [[board[i][i] for i in range(4)], [board[i][3 - i] for i in range(4)]]]
    for d in (a, b, c):
        for line in d:
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

results = ["X won", "O won", "Draw", "Game has not completed"]
ans = []
lines = sys.stdin.readlines()
n = len(lines)
for idx, board in enumerate((lines[5 * i : 5 * (i + 1)] for i in range(n // 5)), 1):
    ans.append(f"Case #{idx}: {results[check(board[1:])]}")
print("\n".join(ans))