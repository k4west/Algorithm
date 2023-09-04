def solution(s, n1, n2):
    s = list(s)
    s[n1], s[n2] = s[n2], s[n1]
    return "".join(s)