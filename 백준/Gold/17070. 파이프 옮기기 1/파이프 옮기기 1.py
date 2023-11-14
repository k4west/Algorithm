import sys
input = sys.stdin.readline

N = int(input())
graph = [['0']]
count = 0
for _ in range(N):
    graph.append(['0']+input().rstrip().split()+['1'])
graph.append(['1']*(N+2))

if graph[N][N] == '1' or (graph[N-1][N] == '1' and graph[N][N-1] == '1'):
    print(0)
    exit()

q = [(1, 2, 'r')]
while q:
    i, j, s = q.pop()
    if i == j == N:
        count += 1
        continue
    A = graph[i][j+1] == '0'
    B = graph[i+1][j] == '0'
    C = graph[i+1][j+1] == '0'
    if A and s != 'c':
        q.append((i, j+1, 'r'))
    if B and s != 'r':
        q.append((i+1, j, 'c'))
    if A and B and C:
        q.append((i+1, j+1, 'd'))

print(count)