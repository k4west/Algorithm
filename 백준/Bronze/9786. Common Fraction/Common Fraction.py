def gcd(a,b):
    while b:a,b=b,a%b
    return a
n,*o=map(int,open(0).read().split())
t=[]
for i in range(n):
    a,b=o[2*i:2*i+2]
    d=gcd(a,b)
    t.append(f'{a//d} {b//d}')
print('\n'.join(t))