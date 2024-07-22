def main():
    s=[*map(int, list(input()))]
    n=len(s)
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+s[i]
    i=n-n%2
    for i in range(n-n%2,0,-2):
        for j in range(n-i+1):
            t=S[j+i//2]
            if t-S[j]==S[j+i]-t:
                print(i)
                return
main()