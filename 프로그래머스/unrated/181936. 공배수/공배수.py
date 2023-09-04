def solution(number, n, m):
    return [0,1][number % n == number % m == 0]