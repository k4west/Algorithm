def solution(s):
    answer = ''
    d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    tmp = ''
    for i in s:
        if i in '0123456789':
            answer += i
        else:
            tmp += i
            if tmp in d:
                answer += d[tmp]
                tmp = ''
    return int(answer)