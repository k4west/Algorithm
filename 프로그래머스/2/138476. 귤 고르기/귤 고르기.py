from collections import Counter
def solution(k, tangerine):
    answer = tmp = 0
    for (size, value) in Counter(tangerine).most_common():
        if k > tmp + value:
            tmp += value
            answer += 1
        else:
            return answer+1