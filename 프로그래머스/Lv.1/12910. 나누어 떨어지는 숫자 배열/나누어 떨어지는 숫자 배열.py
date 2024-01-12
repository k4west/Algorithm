def solution(arr, divisor):
    if (li:=sorted([a for a in arr if not a % divisor])):
        return li
    else:
        return [-1]