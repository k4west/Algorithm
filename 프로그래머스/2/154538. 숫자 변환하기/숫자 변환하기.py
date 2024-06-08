def solution(x, y, n):
    if x==y:return 0
    dp=[-1]*y+[0]
    a=[y]
    v={y}
    while a:
        t=a.pop(0)
        if t==x:break
        for i in (3, 2): 
            if t%i==0 and (j:=t//i) not in v and j>=x:
                dp[j]=dp[t]+1
                a.append(j)
                v.add(j)
        if (j:=t-n) not in v and j>=x:
            dp[j]=dp[t]+1
            a.append(j)
            v.add(j)
    return dp[x]