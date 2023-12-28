import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    in_num, v = [0]*(N+1), [False]*(N+1)
    v[0] = True

    for _ in range(M):
        n, *order = map(int, input().split())
        p = order[0]
        for i in range(1, n):
            graph[p].append((np:=order[i]))
            in_num[np] += 1
            p = np

    q = deque([])
    for i in range(1, N+1):
        if not in_num[i]:
            q.append(i)
    
    ans = []
    while q:
        n = q.popleft()
        if v[n]:
            ans = [0]
            break
        ans.append(n)
        v[n] = True
        for i in graph[n]:
            in_num[i] -= 1
            if not in_num[i]:
                q.append(i)

    if False in v:
        print(0)
    else:
        print(*ans, sep='\n')

if __name__ == "__main__":
    main()