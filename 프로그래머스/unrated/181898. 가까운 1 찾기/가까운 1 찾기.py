def solution(arr, idx):
    for i, a in enumerate(arr[idx:]):
        if a == 1:
            return i + idx
    return -1