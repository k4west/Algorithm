def solution(X, Y):
    li = []
    for s in "0123456789":
        li.extend([s]*min(X.count(s), Y.count(s)))
    a = "".join(li[::-1])
    if not a:
        a = "-1"
    elif a[0] == '0':
        a = '0'
    return a