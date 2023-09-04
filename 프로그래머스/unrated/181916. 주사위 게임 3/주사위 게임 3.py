def solution(a, b, c, d):
    li = [a,b,c,d]
    se = list(set(li))+[0]
    answer = (1111*a, 
              ((5*(sum(li)-sum(se))+(3*sum(se)-sum(li))//2)**2,sum(se)*abs(se[0]-se[1])), 
              a*b*c*d//max(1, (sum(li)-sum(se))**2), 
              min(li))

    return answer[len(se)-2] if len(se) != 3 else answer[len(se)-2][int(sum(li)==2*sum(se))]