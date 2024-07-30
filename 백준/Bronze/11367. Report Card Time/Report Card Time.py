def g(s):
    if s==100:
        return 'A+'
    elif s>=90:
        return 'A'+'+'*(s%10>=7)
    elif s>=80:
        return 'B'+'+'*(s%10>=7)
    elif s>=70:
        return 'C'+'+'*(s%10>=7)
    elif s>=60:
        return 'D'+'+'*(s%10>=7)
    else:
        return 'F'
n,*a=open(0)
t=[]
for i in a:
    name,score=i.split()
    t.append(f'{name} {g(int(score))}')
print('\n'.join(t))