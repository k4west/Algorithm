def solution(n):
    return int("".join(sorted(str(n), reverse=True)))
    # return int("".join(map(str, sorted(map(int, str(n)))[::-1])))