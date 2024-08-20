n,*a=open(0)
t=[]
p=0
for i in a:
    h,m=map(int,i.split(':'))
    if 390<=(j:=h*60+m)<=1140:t.append(j)
if t:t.sort();s,e=t[0],t[-1];p=[24000,36000,16800,24000][2*(s>600)+(e>960)]
print(p)