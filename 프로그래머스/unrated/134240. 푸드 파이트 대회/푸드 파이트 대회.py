def solution(food):
    s = ''
    for i, n in enumerate(food[1:]):
        s += str(i+1)*(n//2)
    return s+'0'+s[::-1]