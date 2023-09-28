def solution(name, yearning, photo):
    d = {k:v for k, v in zip(name, yearning)}
    return [sum((d.get(name, 0) for name in names)) for names in photo] 