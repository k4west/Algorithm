from sys import stdin
def g(N):
    return int(N**0.5) == N**0.5
def f(N):
    if g(N):
        return 1
    for i in range(1, int(N**0.5)+1):
        if g(N-i**2):
            return 2
    while N%4==0:
        N//=4
    return 4 if N%8==7 else 3
print(f(int(stdin.readline())))