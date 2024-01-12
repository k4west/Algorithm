def solution(a, b):
    # return sum(range(min(a, b), max(a, b)+1))
    return (a+b)*(max(a, b)-min(a, b)+1)//2
