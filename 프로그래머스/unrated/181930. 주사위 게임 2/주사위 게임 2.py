def solution(a, b, c):
    return eval("*".join(['(a+b+c)','(a**2+b**2+c**2)','(a**3+b**3+c**3)'][:min(3,int(a==b)+int(b==c)+int(c==a)+1)]))