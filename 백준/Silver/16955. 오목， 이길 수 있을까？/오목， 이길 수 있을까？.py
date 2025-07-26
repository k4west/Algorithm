def check(row):
    d = {'.': 0, 'X': 0, 'O': 0}
    s = 0
    for i, j in enumerate(row):
        if j == 'X':
            d['X'] += 1
        elif j == '.':
            d['.'] += 1
        if i >= 5:
            d[row[s]] -= 1
            s += 1
        if d['X'] == 4 and d['.'] == 1:
            return 1
    return 0

def main():
    board = [input() for _ in range(10)]
    for i in range(10):
        row = board[i]
        if check(row) or check([row[i] for row in board]):
            return 1   
    for i in range(10):
        if i < 6:   # \ 대각선
            for j in range(6):
                if check([board[i+k][j+k] for k in range(10-max(i, j))]):
                    return 1
        if i > 3:   # / 대각선
            for j in range(6):
                if check([board[i-k][j+k] for k in range(min(i+1, 10-j))]):
                    return 1
    return 0

print(main())
