def solution(a, b):
    return [[abs(a-b), a**2+b**2][a%2==1], 2*(a+b)][(a+b)%2==1]