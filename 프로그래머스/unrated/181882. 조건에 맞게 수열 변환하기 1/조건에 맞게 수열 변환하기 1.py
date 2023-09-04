def solution(arr):
    return [a/2 if a>=50 and a%2==0 else a*2 if a<50 and a%2==1 else a for a in arr]