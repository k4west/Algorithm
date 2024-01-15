def solution(s):
    ans = ''
    flag = True
    for i in s:
        if i == ' ':
            ans += i
            flag = True
        elif flag:
            ans += i.upper()
            flag = False
        else:
            ans += i.lower()
    return ans