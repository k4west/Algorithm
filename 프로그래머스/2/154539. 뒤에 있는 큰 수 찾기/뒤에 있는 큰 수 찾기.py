def solution(numbers):
    s=[];a=[-1]*(n:=len(numbers))
    for i in range(n-1):
        if numbers[i]<(t:=numbers[i+1]):
            a[i]=t
            while s and numbers[s[-1]]<t:a[s.pop()]=t
        else:s.append(i)
    return a