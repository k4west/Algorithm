from collections import deque
def main():
    a = open(0)
    N = int(next(a))
    graph = [[] for _ in range(N+1)]
    ans = [[] for _ in range(N+1)]
    for _ in range(N-1):
        i, j = map(int, next(a).split())
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
main()