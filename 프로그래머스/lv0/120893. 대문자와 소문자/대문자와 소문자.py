def solution(my_string):
    return "".join([s.upper() if s.islower() else s.lower() for s in my_string])