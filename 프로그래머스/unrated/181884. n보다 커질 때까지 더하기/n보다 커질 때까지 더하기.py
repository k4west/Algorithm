def solution(numbers, n):
    a = 0
    for s in numbers:
        a += s
        if a > n:
            return a