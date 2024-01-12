def solution(left, right):
    s = 0
    for n in range(left, right+1):
        if (n**.5)%1:
            s += n
        else:
            s -= n
    return s