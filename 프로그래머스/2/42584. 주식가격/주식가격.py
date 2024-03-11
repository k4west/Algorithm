def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n-1):
        p = prices[i]
        t = 0
        for j in range(i+1, n):
            if p > prices[j]:
                break
        answer.append(j-i)
        
    return answer + [0]