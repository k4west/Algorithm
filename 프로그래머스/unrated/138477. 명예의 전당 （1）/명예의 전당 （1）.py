def solution(k, score):
    li = []
    a = []
    for i, s in enumerate(score):
        li.append(s)
        li.sort()
        a.append(li[max(-i-1, -k)])
    return a