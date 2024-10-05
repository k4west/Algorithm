def f(s, e):
    v = [0] * 21
    c = 0
    q, nq = [s], []
    while q or nq:
        c += 1
        for i in q:
            v[i] = 1
            for j in graph[i]:
                if j == e: return c
                if not v[j]:
                    nq.append(j)
                    v[j] = 1
        q, nq = nq, []
        
a = open(0)
result = []
n = 1
while a:
    graph = [[] for _ in range(21)]
    for i in range(1, 20):
        try:
            X, *countries = map(int, next(a).split())
        except:
            exit(print('\n\n'.join(result)))
        for j in countries:
            graph[i].append(j)
            graph[j].append(i)
    temp = [f'Test Set #{n}']
    for _ in range(int(next(a))):
        s, e = map(int, next(a).split())
        c = f(s, e)
        temp.append(f'{str(s).rjust(2, " ")} to {str(e).rjust(2, " ")}: {c}')
    result.append('\n'.join(temp))
    n += 1