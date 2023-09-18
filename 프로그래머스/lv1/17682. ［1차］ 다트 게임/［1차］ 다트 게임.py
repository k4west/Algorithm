def solution(dartResult):
    t = []
    for i in dartResult:
        if i.isdigit():
            if t and t[-1] == 1 and i =='0':
                t[-1] = 10
            else:
                t.append(int(i))
        elif i.isalpha():
            if i == 'D':
                t[-1] **= 2
            elif i == 'T':
                t[-1] **= 3
        else:
            if i == "*":
                t[-1] *= 2
                if len(t) > 1:
                    t[-2] *= 2
            elif i == "#":
                t[-1] *= -1
    return sum(t)