def solution(numbers, direction):
    return {'right': [numbers[-1]]+numbers[:-1], 'left': numbers[1:]+[numbers[0]]}[direction]