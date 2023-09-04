def solution(a, b):
    return int(max("".join(map(str,(a,b))), "".join(map(str,(b,a)))))