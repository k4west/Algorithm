def solution(my_string):
    return ''.join([s for s in my_string if not s in 'aeiou'])