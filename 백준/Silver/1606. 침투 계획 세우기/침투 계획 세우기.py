import sys
a, b = map(int, sys.stdin.readline().split())
if a<=0 and b<=0: print(3*(a+b)**2-b+1)
elif a>=0 and b>0: print(3*(a+b)**2-3*a-2*b+1)
elif a>=-b>=0: print(3*a*(a+1)+b+1)
elif -b>a>0: print(3*b**2-b+a+1)
elif -a>=b>0: print(3*a**2-b+1)
else: print(3*b**2-a-2*b+1)