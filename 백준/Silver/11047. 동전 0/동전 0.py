import sys
input = sys.stdin.readline

N, K = map(int, input().split())
C = []
for i in range(N):
    c = int(input())
    if c <= K:
        C.append(c)

answer = 0
while K > 0:
    answer += K // C[-1]
    K %= C[-1]
    C.pop()
print(answer)