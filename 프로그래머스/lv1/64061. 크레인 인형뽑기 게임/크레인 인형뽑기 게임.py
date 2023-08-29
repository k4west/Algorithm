def solution(board, moves):
    count = 0
    stack = []
    for m in moves:
        m -= 1
        for i in range(len(board)):
            if board[i][m] != 0:
                temp = board[i][m]
                board[i][m] =  0
                if stack and temp == stack[-1]:
                    stack.pop()
                    count += 2
                else:
                    stack.append(temp)
                break
    return count