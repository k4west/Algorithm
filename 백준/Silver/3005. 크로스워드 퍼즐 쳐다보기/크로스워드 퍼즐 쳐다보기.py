R, C = map(int, input().split())
graph = [input() for _ in range(R)]
t = []
for r in range(R):
    s = ''
    count = 0
    for i in graph[r]:
        if i =='#':
            if count>1:
                t.append(s)
            s = ''
            count = 0
        else:
            s += i
            count += 1
    if count>1:
        t.append(s)
for c in range(C):
    s = ''
    count = 0
    for i in graph:
        if (i:=i[c]) =='#':
            if count>1:
                t.append(s)
            s = ''
            count = 0
        else:
            s += i
            count += 1
    if count>1:
        t.append(s)
print(sorted(t)[0])