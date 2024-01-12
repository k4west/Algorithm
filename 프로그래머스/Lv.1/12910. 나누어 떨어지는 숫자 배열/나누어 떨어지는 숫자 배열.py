def solution(arr, divisor):
    return sorted([a for a in arr if not a % divisor]) or [-1]