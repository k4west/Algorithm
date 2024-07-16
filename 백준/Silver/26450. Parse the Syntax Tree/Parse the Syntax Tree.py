_,*a=open(0)
a=list(''.join(a).replace('.','').replace(' ','').replace('\n','')[::-1])
i=0
for j,s in enumerate(a):
    if s in '+-*':
        a[j]="".join(('(',a[i+1],s,a[i],')'))
        i+=2
print(eval(a[-1]))