def solution(num):
    i = 0
    while num != 1:
        if not num % 2:
            num //= 2
        else:
            num = num * 3 + 1
        i += 1
        if i > 500:
            return -1
    return i

    # if num == 1:
    #     return 0
    # for i in range(1, 501):
    #     if not num % 2:
    #         num //= 2
    #     else:
    #         num = num * 3 + 1
    #     if num == 1:
    #         return i
    # return -1