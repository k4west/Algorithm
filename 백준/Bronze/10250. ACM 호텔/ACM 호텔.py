import sys
T = int(input())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    Y = N%H
    X = N//H + 1
    if Y == 0:
        Y = H
        X -= 1
    print(str(Y)+str(X) if X > 9 else str(Y)+'0'+str(X))