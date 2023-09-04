def solution(my_string, is_prefix):
    return int(is_prefix == my_string[:len(is_prefix)])