import sys
from collections import deque
input = sys.stdin.readline
    
def main():
    N = int(input())
    graph = [[] for _ in range(N+1)]
    ans = [[] for _ in range(N+1)]
    for _ in range(N-1):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    q = deque([1])
    while q:
        i = q.popleft()
        for n in graph[i]:
            if not ans[n]: 
                ans[n] = i
                q.append(n)
    print("\n".join(map(str, ans[2:])))

if __name__ == "__main__":
    main()