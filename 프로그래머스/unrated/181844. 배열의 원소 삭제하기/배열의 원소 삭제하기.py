def solution(arr, delete_list):
    for d in delete_list:
        if d in arr:
            arr.remove(d)
    return arr