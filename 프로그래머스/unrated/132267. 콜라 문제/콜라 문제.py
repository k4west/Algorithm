def solution(a, b, n):
    answer = 0
    while n >= a:
        t = n//a * b
        answer += t
        n = t + n%a
    return answer