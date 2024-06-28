d={"1":"Yakk","2":"Doh","3":"Seh","4":"Ghar","5":"Bang","6":"Sheesh"}
s={"1":"Habb Yakk","2":"Dobara","3":"Dousa","4":"Dorgy","5":"Dabash","6":"Dosh"}
_,*a=open(0)
t=[]
for i,j in enumerate(a,1):
    n,m=sorted(j.strip().split())
    if n==m:t.append(f'Case {i}: {s[m]}')
    else:t.append(f'Case {i}: {d[m]} {d[n]}')
print('\n'.join(t).replace('Sheesh Bang', 'Sheesh Beesh'))