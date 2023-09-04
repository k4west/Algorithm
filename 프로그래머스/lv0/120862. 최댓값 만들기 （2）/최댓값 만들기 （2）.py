def solution(numbers):
    answer = 0
    return max(sorted(numbers)[0]*sorted(numbers)[1], sorted(numbers)[-2]*sorted(numbers)[-1])