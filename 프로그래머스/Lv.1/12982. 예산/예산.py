def solution(d, budget):
    answer = 0
    s = 0
    for r in sorted(d):
        s += r
        if s > budget:
            break
        answer += 1
    return answer