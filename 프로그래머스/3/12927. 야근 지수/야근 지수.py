def solution(n, works):
    if n >= (W:=sum(works)):
        return 0
    d={}
    for w in works:d[w]=d.get(w,0)+1
    k=[*d.keys()]
    k.sort()
    while n:
        if n >= d[(t:=k[-1])]:
            n -= d[t]
            if t>1:
                d[t-1]=d.get(t-1,0)+d[t]
                if t-1 not in k: k.append(t-1);k.sort()
            del d[k.pop()]
        else:
            if t>1:
                d[t-1]=d.get(t-1,0)+n
            d[t]-=n
            break
    
    return sum(k*k*v for k, v in d.items())