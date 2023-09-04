def solution(arr):
    return arr[arr.index(2):len(arr)-arr[::-1].index(2)] if 2 in arr else [-1]