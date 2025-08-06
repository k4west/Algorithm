ans = []
N, M = map(int, input().split())
*li, = map(int, input().split())

accumulated = [0]*(N+1)
for i in range(N):
    accumulated[i] = accumulated[i-1] + li[i]

for _ in range(M):
    s, e = map(int, input().split())
    ans.append(accumulated[e-1]-accumulated[s-2])

print('\n'.join(map(str, ans)))