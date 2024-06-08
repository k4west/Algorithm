m=10**9+7
dp={1:1,2:1,3:2,4:3,5:5}
def f(n):
    if n in dp:return dp[n]
    t=n//2
    if n%2:dp[n]=(f(t)**2+f(t+1)**2)%m
    else:dp[n]=(f(t)*(f(t-1)+f(t+1)))%m
    return dp[n]
def solution(n):return f(n+1)