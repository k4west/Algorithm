import sys
input = lambda: int(sys.stdin.readline())
ans = []
for i in range(input()):
    n = input()
    graph = [input() for _ in range(n)]
    c, prev = 1, graph[0]
    for _ in range(n):
        if prev == n: ans.append(str(c)); break
        if t := graph[prev - 1]: graph[prev - 1], prev = 0, t
        else: break
        c += 1
    if len(ans) == i: ans.append('0')
print("\n".join(ans))