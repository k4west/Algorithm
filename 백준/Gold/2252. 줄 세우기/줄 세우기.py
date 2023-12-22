import sys
from collections import deque
input = sys.stdin.readline
    
def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    in_num = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_num[b] += 1

    line = []
    q = deque()

    for i in range(1, N+1):
        if not in_num[i]:
            q.append(i)
    
    while q:
        s0 = q.popleft()
        line.append(str(s0))
        for s1 in graph[s0]:
            in_num[s1] -= 1
            if not in_num[s1]:
                q.append(s1)
    
    print(" ".join(line))

if __name__ == "__main__":
    main()