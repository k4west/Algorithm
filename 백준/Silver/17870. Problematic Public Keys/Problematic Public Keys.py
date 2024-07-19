m,*a=open(0)
p=set()
for n in map(int, a):
    for i in range(2, int(n*.5)+1):
        if n%i==0:
            break
    p.add(i)
    p.add(n//i)
p=sorted(p)
print('\n'.join([' '.join(map(str, p[5*i:5*i+5])) for i in range(len(p)//5+1)]))