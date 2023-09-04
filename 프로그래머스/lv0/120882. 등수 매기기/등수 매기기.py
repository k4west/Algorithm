def solution(score):
    k = [sum(s) for s in score]
    return [sorted(k, reverse=True).index(t)+1 for t in k]