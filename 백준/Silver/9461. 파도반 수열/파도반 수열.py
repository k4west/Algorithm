import sys
T = int(sys.stdin.readline())
P = [0, 1, 1, 1, 2, 2] + [0] * 95
for n in range(6, 101):
            P[n] = P[n-1] + P[n-5]
for _ in range(T):
    print(P[int(sys.stdin.readline())])