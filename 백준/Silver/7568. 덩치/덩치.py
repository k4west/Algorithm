import sys
input = sys.stdin.readline

N = int(input())

P = [[0, 0]] * N
for n in range(N):
    P[n] = list(map(int, input().split()))

answer = [0] * N
for i in range(N):
    c = 1
    for j in range(N):
        if (P[i][0] < P[j][0] and P[i][1] < P[j][1]):
            c += 1
    answer[i] = c

print(*answer)