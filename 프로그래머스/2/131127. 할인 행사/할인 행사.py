def solution(want, number, discount):
    target = {item: num for item, num in zip(want, number)}
    tmp = {item: 0 for item in want}
    for i in range(10):
        if (item:=discount[i]) in tmp:
            tmp[item] += 1
            
    answer = 0    
    if target == tmp:
        answer += 1
    
    n = len(discount)
    while i < n-1:
        if (item:=discount[i-9]) in tmp:
            tmp[item] -= 1
        if (item:=discount[(i:=i+1)]) in tmp:
            tmp[item] += 1
        if target == tmp:
            answer += 1
    return answer