def n_d(n):
    a = set()
    for i in range(1, int(n**.5)+1):
        if n%i==0:
            a.update((i, n//i))
    return len(a)

def solution(number, limit, power):
    s = 0
    for n in range(1, number+1):
        t = n_d(n)
        if t > limit: t = power
        s += t
    return s