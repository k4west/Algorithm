def f(n):
    s = 0
    for i in range(1, int(n**.5)+1):
        if n % i == 0: 
            s += i
            if i != (j:=n//i): s += j
    if 2*n == s:
        return 'Perfect'
    return ('Deficient', 'Abundant')[2*n < s]
input()
print("\n".join((f(n) for n in map(int, input().split()))))