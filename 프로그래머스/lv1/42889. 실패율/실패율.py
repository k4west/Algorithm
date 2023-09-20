def solution(N, stages):
    li = [0]*(N+2)
    n = len(stages)
    for stage in stages:
        li[stage] += 1
    arr = []
    for i in range(1, N+1):
        if n:
            arr.append([i, li[i]/n])
            n -= li[i]
        else: 
            arr.append([i, 0])
    arr = sorted(arr, key=lambda x:-x[1])
    answer = [a[0] for a in arr]
    return answer