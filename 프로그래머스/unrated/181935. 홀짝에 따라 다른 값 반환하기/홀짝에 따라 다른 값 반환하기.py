def solution(n):
    return ((n+1)/2)**2 if n%2==1 else 2*(n//2)*(n//2+1)*(n+1)//3