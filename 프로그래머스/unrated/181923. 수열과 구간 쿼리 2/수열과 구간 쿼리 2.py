def solution(arr, queries):
    return [min([a for a in arr[s:e+1] if a > k] or [-1]) for s, e, k in queries]