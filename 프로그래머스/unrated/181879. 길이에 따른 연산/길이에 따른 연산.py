def solution(num_list):
    return eval('+*'[len(num_list)<=10].join(str(n) for n in num_list))