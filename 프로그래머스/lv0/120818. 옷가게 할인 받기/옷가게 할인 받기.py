def solution(price):
    if price >= 500000:
        i = 0.2
    elif price >= 300000:
        i = 0.1
    elif price >= 100000:
        i = 0.05
    else:
        i = 0
    return int(price * (1 - i))