def solution(word):
    d = {t:i for i, t in enumerate('AEIOU')}
    return sum((5**(5-i)//4)*d[t] + 1 for i, t in enumerate(word))
