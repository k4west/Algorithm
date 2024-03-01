N,L,W,H=map(int,input().split())
l,r=0,(L*W*H/N)**(1/3)
for _ in range(40):
    if(L//(m:=(l+r)/2))*(W//m)*(H//m)<N:r=m
    else:l=m
print(f"{l:.9f}")