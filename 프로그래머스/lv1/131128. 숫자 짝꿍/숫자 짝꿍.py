def solution(X, Y):
    x, y = [0]*10, [0]*10
    for s in "0123456789":
        x[int(s)] = X.count(s)
        y[int(s)] = Y.count(s)
    li = []
    for i, s in enumerate(zip(x,y)):
        li.extend([i]*min(s))
    a = "".join(map(str,li[::-1]))
    if not a:
        a = "-1"
    elif a[0] == '0':
        a = '0'
    return a