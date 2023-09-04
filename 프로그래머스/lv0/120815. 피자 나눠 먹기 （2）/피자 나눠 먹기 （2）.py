def solution(n):
    return n // 6 if n%6==0 else n//2 if n%2==0 else n//3 if n%3==0 else n    