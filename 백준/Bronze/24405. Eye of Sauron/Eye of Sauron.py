s=input()
n=len(s)
print(['fix','correct'][n%2==0 and s[n//2-1]=='('])