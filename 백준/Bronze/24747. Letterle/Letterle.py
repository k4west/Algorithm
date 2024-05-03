L=next(a:=open(0)).strip()
for i, G in enumerate(a):
    t=''
    for l, g in zip(L, G):
        if l==g: t+='G'
        elif g in L: t+='Y'
        else: t+='X'
    if t=='G'*5: print('WINNER'); exit()
    elif i<6: print(t)
    else: print('LOSER')