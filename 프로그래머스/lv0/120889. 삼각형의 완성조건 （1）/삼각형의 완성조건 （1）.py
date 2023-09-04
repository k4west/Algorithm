def solution(sides):
    return [2,1][sum(sides) > 2 * max(sides)]