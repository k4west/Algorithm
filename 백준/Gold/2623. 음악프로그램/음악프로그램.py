import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    in_num, v = [0]*(N+1), set(range(1, N+1))

    for _ in range(M):
        n, *order = map(int, input().split())
        for i in range(0, n-1):
            graph[order[i]].append((t:=order[i+1]))
            in_num[t] += 1
            v.discard(t)

    q = deque(list(v))    
    ans = []
    while q:
        n = q.popleft()
        ans.append(str(n))
        for i in graph[n]:
            in_num[i] -= 1
            if not in_num[i]:
                q.append(i)

    if len(ans) != N:
        print(0)
    else:
        print('\n'.join(ans))

if __name__ == "__main__":
    main()