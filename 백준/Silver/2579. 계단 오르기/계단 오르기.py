import sys
input = sys.stdin.readline

N = int(input())
S = [0]
R = [0] * (N + 1)
for _ in range(N):
    S.append(int(input()))

if N == 1:
    print(S[1])
else:
    R[1] = S[1]
    R[2] = S[1] + S[2]

    for i in range(3, N + 1):
        R[i] = max(R[i - 3] + S[i - 1], R[i - 2]) + S[i]

    print(R[N])