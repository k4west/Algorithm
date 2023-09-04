def solution(arr, queries):
    for s, e in queries:
        arr = [arr[i] + 1 if s <= i <= e  else arr[i] for i in range(len(arr))]
    return arr