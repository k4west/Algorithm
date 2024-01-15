def solution(s):
    ans = ''
    flag = True
    for i in s:
        if i == ' ':
            ans += i
            flag = True
        elif flag:
            if i.isdigit():
                ans += i
            else:
                ans += i.upper()
            flag = False
        else:
            ans += i.lower()
    return ans
    
    # if s == ' ':
    #     return ' '
    # return " "*(s[0]==' ') + " ".join(word[0].upper() + word[1:].lower() for word in s.split()) + " "*(s[-1]==' ')