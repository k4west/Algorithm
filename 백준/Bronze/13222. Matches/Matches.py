n,*a=open(0)
_,w,h=map(float,n.split())
m=(w**2+h**2)**.5
print('\n'.join(['YNEOS'[i>m::2] for i in map(float,a)]))