def solution(s):
    answer = ''
    INF = float('inf')
    m, M = INF, -INF 
    for i in map(int, s.split()):
        if i > M:
            M = i
        if i < m:
            m = i
    return f"{m} {M}"