import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_num, v = [0]*(N+1), set(range(1, N+1))

for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        graph[order[i]].append((t:=order[i+1]))
        in_num[t] += 1
        v.discard(t)

s = list(v)
ans = []
while s:
    n = s.pop()
    ans.append(str(n))
    for i in graph[n]:
        in_num[i] -= 1
        if not in_num[i]:
            s.append(i)

if len(ans) != N:
    print(0)
else:
    print('\n'.join(ans))