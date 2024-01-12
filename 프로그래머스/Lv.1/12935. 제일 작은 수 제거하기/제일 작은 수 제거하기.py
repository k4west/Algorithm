def solution(arr):
    del arr[arr.index(min(arr))]
    return arr or [-1]