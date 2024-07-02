H,M=map(int, input().split(':'))
t=H*60+M
if 300<t<420:
    if (d:=t-300)<=90:t=2*t-180
    else:t=510+d
elif 420<=t<600:t=420+t//2
elif 780<t<900:
    if (d:=t-780)<=120:t=2*t-660
    else:t=1020+d
elif 900<=t<1140:t=690+t//2
else:t+=120
h=t//60
m=t%60
print(f'{h%24:02}:{m:02}')