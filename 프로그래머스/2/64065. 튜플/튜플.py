def solution(s):
    answer = []
    t = sorted([eval(t) for t in s[1:-1].replace('},{','} {').split()])
    q=set()
    for p in t:answer.append(*(p-q));q=p
    return answer