a,b,c,d,e,f=map(int,input().split())
t=a*e-b*d
print((c*e-b*f)//t,(a*f-c*d)//t)