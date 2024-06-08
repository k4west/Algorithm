m=10007
d={1:1,2:1,3:2,4:3,5:5}
def f(n):
    if n in d:return d[n]
    t=n//2
    if n%2:d[n]=(f(t)**2+f(t+1)**2)%m
    else:d[n]=(f(t)*(f(t-1)+f(t+1)))%m
    return d[n]
print(f(int(input())+1))