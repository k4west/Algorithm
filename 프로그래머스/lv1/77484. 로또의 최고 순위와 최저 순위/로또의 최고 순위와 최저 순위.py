def solution(lottos, win_nums):
    a, b = 7, 0
    for i in lottos:
        if i in win_nums:
            a -= 1
        if not i:
            b -= 1
    return [min(a+b, 6), min(a, 6)]