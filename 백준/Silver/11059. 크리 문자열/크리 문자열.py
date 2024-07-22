def main():
    s=[*map(int, list(input()))]
    n=len(s)
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+s[i]
    i=n-n%2
    flag = False
    while i:
        for j in range(n-i+1):
            if S[j+i//2]-S[j] == S[j+i]-S[j+i//2]:
                print(i)
                return
        if flag:
            break
        i -= 2
    print(i)
main()