def solution(numbers):
    s=[]
    n=len(numbers)
    a=[-1]*n
    m=numbers[0]
    for i in range(n-1):
        if numbers[i]<(t:=numbers[i+1]):
            a[i]=t
            for _ in range(len(s)):
                if numbers[(j:=s.pop())]>=t:
                    s.append(j)
                    break
                a[j]=t
        else:s.append(i)
    return a