_,*a=map(lambda x: float(x)%2, open(0).read().split())
n=len(a)
se=so=to=te=0
for odd in a:
    if odd:
        so+=to
        te+=1
        if to:
            to=1
    else:
        se+=te
        to+=1
        if te:
            te=1
print(min(se,so))