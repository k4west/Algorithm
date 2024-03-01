N,L,W,H=map(int,input().split())
l,r=0,min(L,W,H)
for _ in range(40):
    if(L//(m:=(l+r)/2))*(W//m)*(H//m)<N:r=m
    else:l=m
print(f"{l:.9f}")