from sys import stdin
def f(N):
    if int(N**0.5) == N**0.5:
        return 1
    s = {i**2 for i in range(1, int(N**0.5)+1)}
    for i in s:
        if N-i in s:
            return 2
    while N%4==0:
        N//=4
    return 4 if N%8==7 else 3
print(f(int(stdin.readline())))