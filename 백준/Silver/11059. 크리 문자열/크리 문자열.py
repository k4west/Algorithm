def check(li, n):
    return sum(li[:n]) == sum(li[n:])

def main():
    S=[*map(float, list(input()))]
    n=len(S)
    i=n-n%2
    flag = False
    while i:
        for j in range(n-i+1):
            if check(S[j:j+i], i//2):
                print(i)
                return
        if flag:
            break
        i -= 2
    print(i)

main()