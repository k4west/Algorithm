def solution(arr1, arr2):
    return [[a1+a2 for a1, a2 in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]