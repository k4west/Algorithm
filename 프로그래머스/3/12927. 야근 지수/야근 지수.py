def solution(n, works):
    if n >= sum(works):
        return 0
    
    d={}
    for w in works:
        d[w] = d.get(w,0)+1
        
    li = [0]*((m:=max(d))+1)
    for k,v in d.items():
        li[k] = v
    
    for i in range(1, m+1):
        if (t:=li[-i]):
            if t < n:
                n -= t
                li[-i] = 0
                li[-i-1] += t
            else:
                li[-i] -= n
                li[-i-1] += n
                break
                
    return sum(k*k*v for k, v in enumerate(li) if v)