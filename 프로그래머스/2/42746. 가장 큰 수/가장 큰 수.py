# from functools import cmp_to_key as ck
# def solution(numbers):
#     return str(int("".join(sorted(map(str, numbers), key=ck(lambda x,y: 2*(x+y>y+x) -1))[::-1])))

def solution(numbers):
    return str(int("".join(sorted(map(str, numbers), key=lambda x: x*4)[::-1])))