def solution(arr, intervals):
    li = []
    for s, e in intervals:
        li += arr[s:e+1]
    return li