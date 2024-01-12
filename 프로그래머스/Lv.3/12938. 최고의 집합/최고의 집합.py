def solution(n, s):
    if s-n+1 <= 0: return [-1]
    ans = []
    for i in range(n, 0, -1): 
        ans.append(t:=s//i)
        s -= t
    return ans