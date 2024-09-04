def sol(board):
    for i in range(6):
        if 6!=len(set(board[6*i:6*(i+1)])):return 0
        if 6!=len(set(board[i:36:6])):return 0
        j=i//2*12+i%2*3
        if 6!=len(set(board[j:j+3]+board[j+6:j+9])):return 0
    if 6!=len(set(board[::7])):return 0
    if 6!=len(set(board[5::5])):return 0
    return 1
n,*a=map(int,open(0).read().split())
print('\n'.join([f'Case#{i+1}: {sol(a[36*i:36*(i+1)])}' for i in range(n)]))