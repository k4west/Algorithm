def solution(clothes):
    d = {}
    for cloth, types in clothes:
        if types in d:
            d[types].append(cloth)
        else:
            d[types] = [cloth]
    s = 1
    for i in d.values():
        s *= len(i) + 1
    return s - 1