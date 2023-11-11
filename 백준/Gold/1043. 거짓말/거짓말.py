import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nk, *stack = map(int, input().split())
meeting, count = [], 0
graph = {i: set() for i in range(1, N+1)}
if not nk:
    for _ in range(M): input()
    print(M)
else:
    for _ in range(M):
        _, *m = map(int, input().split())
        meeting.append(m)
        for n1 in m:
            for n2 in m:
                graph[n1].add(n2)
                graph[n2].add(n1)

    know = set(stack)
    while stack:
        n = stack.pop()
        know.add(n)
        m = graph[n]
        if not m - know:
            continue
        for p in m:
            if p in know:
                stack.extend(list(m - know))
    for m in meeting:
        if not set.intersection(know, m):
            count += 1

    print(count)