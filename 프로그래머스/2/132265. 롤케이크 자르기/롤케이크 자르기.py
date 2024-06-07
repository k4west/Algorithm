def solution(topping):
    l,r,v,w,t=[],[0]*(n:=len(topping)),set(),set(),0
    for i in range(n):
        v.add(topping[i])
        w.add(topping[-i-1])
        l.append(len(v))
        r[-i-1]=len(w)
    return sum(l[i]==r[i+1] for i in range(1,n-1))