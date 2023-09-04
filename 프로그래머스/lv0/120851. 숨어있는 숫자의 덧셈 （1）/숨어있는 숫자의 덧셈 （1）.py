def solution(my_string):
    return eval("+".join([s for s in my_string if s.isdigit()]))