def solution(n, wires):
    if n <= 3:
        return n-2
    
    def find_root(x):
        if x != (t:=roots[x]):
            roots[x] = find_root(t)
        return roots[x]
    
    def union_root(x, y):
        if x < y:
            roots[y] = x
        else:
            roots[x] = y
    
    answer = 100
    for i in range(n-1):
        roots = [i for i in range(n+1)]
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue
            if (x:=find_root(a)) != (y:=find_root(b)):
                union_root(x, y)
        for i in range(1, n+1):
            find_root(i)
    
        d = {s:0 for s in set(roots[1:])}
        for i in roots[1:]:
            d[i] += 1

        li = list(d.values())
        if answer > (m:=abs(li[0] - li[-1])):
            answer = m
    return answer