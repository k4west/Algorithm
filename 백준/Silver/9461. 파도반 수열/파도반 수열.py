import sys
T = int(sys.stdin.readline())
P = [0, 1, 1, 1, 2, 2]
for _ in range(T):
    N = int(sys.stdin.readline())
    if N > 5:
        P += [0]*(N-5)
        for n in range(6, N+1):
            P[n] = P[n-1] + P[n-5]
    print(P[N])