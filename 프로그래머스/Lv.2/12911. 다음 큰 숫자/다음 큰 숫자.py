def solution(n):
    one = bin(n).count('1')
    print(one)
    for i in range(1, n):
        if one == bin(t:=n + i).count('1'):
            return t