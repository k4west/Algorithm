def solution(elements):
    v = set()
    n = len(elements)
    elements += elements
    for i in range(1, n+1):
        for s in range(n):
            v.add(sum(elements[s:s+i]))
    return len(v)