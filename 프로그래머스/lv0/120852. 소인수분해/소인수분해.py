def solution(n):
    m=n
    li=[]
    for i in range(2,n+1):
        if m%i==0:
            while m%i==0:
                m //= i
            li.append(i)
    return li