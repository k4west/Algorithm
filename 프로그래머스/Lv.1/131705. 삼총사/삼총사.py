def solution(number):
    n = len(number)
    c = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if not number[i] + number[j] + number[k]:
                    c += 1
    return c