from itertools import permutations, islice
def solution(word):
    answer = 0
    d = {t:i for i, t in enumerate('AEIOU')}
    for i, t in enumerate(word):
        f = 0
        for j in range(5-i):
            f += 5 ** j
        answer += f*d[t] + 1
    return answer