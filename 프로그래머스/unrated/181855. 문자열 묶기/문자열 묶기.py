def solution(strArr):
    a = [0] * 30
    for s in strArr:
        a[len(s)-1] += 1
    return max(a)