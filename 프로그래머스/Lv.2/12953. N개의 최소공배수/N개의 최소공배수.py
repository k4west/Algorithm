from math import gcd

def solution(arr):
    a = arr[0]
    for b in arr[1:]:
        a = a*b//gcd(a, b)
    return a