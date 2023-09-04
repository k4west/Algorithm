def solution(num_list):
    return int("".join(str(n) for n in num_list if n % 2 == 1)) + int("".join(str(n) for n in num_list if n % 2 == 0))