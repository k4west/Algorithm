a=open(0)
r=[]
for i in range(int(next(a))):
    s,w,p,t=map(int,next(a).split())
    suspects=[]
    places=[set() for _ in range(s+1)]
    outtime=[[[] for _ in range(p+1)] for _ in range(s+1)]
    intime=[[[] for _ in range(p+1)] for _ in range(s+1)]
    for _ in range(w):
        S,P,b,f=map(int,next(a).split())
        if b<=t<=f:
            places[S].add(P)
            intime[S][P].append([b, f])
        else:
            outtime[S][P].append([b, f])
    for S in range(1, s+1):
        if len(P:=places[S])!=1:
            suspects.append(S)
        else:
            P0=[*P][0]
            check=True
            for b0, f0 in intime[S][P0]:
                flag=False
                for P1 in range(1,p+1):
                    if P0==P1:
                        continue
                    for b1, f1 in outtime[S][P1]: 
                        if b0<=b1<=f0 or b0<=f1<=f0 or b1<=b0<=f1 or b1<=f0<=f1:
                            flag=True
                            break
                    if flag:
                        break
                if not flag:
                    check=False
                    break
            if check:
                suspects.append(S)
    suspects='\n'.join(map(str,suspects)) or 'No suspect.'
    r.append(f'Data Set {i+1}:\n{suspects}')
print('\n\n'.join(r))