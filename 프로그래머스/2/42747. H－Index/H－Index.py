def solution(citations):
    i = 1
    while True:
        if i > sum(1 for c in citations if c >= i):
            return i-1
        i += 1
    