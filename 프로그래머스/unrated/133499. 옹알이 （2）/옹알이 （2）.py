import re
def solution(babbling):
    s = 0
    for b in babbling:
        b = re.sub("ayaaya|yeye|woowoo|mama","n",b)
        b = re.sub("aya|ye|woo|ma","",b)
        if not b:
            s += 1
    return s