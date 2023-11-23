import sys
from collections import deque
input = sys.stdin.readline

def an():
    q = deque()
    q.append(N)
    while q:
        n = q.popleft()
        if n == K:
            print(answer[n])
            break
        for i in (n -1, n + 1, 2 * n): 
            if 0 <= i <= M and not answer[i]:
                q.append(i)
                answer[i] = answer[n] + 1

N, K = map(int, input().split())
M = 10 ** 5
answer = [0] * (M + 1)

an()