def solution(arr, k):
    li = []
    for a in arr:
        if a not in li:
            li.append(a)
            if len(li) == k:
                break
    return li+ [-1]*(k-len(li))