def solution(s, n):
    ans = ''
    for i in s:
        if (k:=ord(i)) in range(65, 91):
            x = k+n
            if x > 90:
                x -= 26
            ans += chr(x)
        elif k in range(97, 123):
            x = k+n
            if x > 122:
                x -= 26
            ans += chr(x)
        else:
            ans += i
    return ans