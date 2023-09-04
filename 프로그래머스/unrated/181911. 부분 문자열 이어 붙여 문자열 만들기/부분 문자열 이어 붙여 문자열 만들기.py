def solution(my_strings, parts):
    return "".join([my_strings[i][p[0]:p[1]+1] for i, p in enumerate(parts)])