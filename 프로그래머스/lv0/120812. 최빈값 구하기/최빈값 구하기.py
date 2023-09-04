def solution(array):
    d = {a:array.count(a) for a in set(array)}
    if list(d.values()).count(max(d.values())) != 1:
        return -1
    else: 
        return list(d.keys())[list(d.values()).index(max(d.values()))]
