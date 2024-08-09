def g(p,i,o,P):
    for b, f in i:
        fg=False
        for P1 in range(1,p+1):
            if P==P1:continue
            for b1, f1 in o[P1]: 
                if b<=b1<=f or b<=f1<=f or b1<=b<=f1 or b1<=f<=f1:fg=True;break
            if fg:break
        if not fg:return False
    return True
a=open(0)
r=[]
for i in range(int(next(a))):
    s,w,p,t=map(int,next(a).split())
    ss=[]
    ps=[set() for _ in range(s+1)]
    ot=[[[] for _ in range(p+1)] for _ in range(s+1)]
    it=[[[] for _ in range(p+1)] for _ in range(s+1)]
    for _ in range(w):
        S,P,b,f=map(int,next(a).split())
        if b<=t<=f:ps[S].add(P);it[S][P].append([b,f])
        else:ot[S][P].append([b,f])
    for S in range(1,s+1):
        if len(P:=ps[S])!=1:ss.append(S)
        elif g(p,it[S][[*P][0]],ot[S],P):ss.append(S)
    ss='\n'.join(map(str,ss)) or 'No suspect.'
    r.append(f'Data Set {i+1}:\n{ss}')
print('\n\n'.join(r))