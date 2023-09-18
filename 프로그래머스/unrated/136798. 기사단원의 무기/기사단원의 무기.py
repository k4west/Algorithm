def n_d(n):
    k = 1
    for i in range(2, int(n**.5)+1):
        c = 1
        while n%i==0:
            c+=1
            n//=i
        k *= c
    if n != 1: k *= 2
    return k

def solution(number, limit, power):
    s = 0
    for n in range(1, number+1):
        t = n_d(n)
        if t > limit: t = power
        s += t
    return s