def solution(myString):
    return [s for s in sorted(list(myString.split("x"))) if s.isalpha()]