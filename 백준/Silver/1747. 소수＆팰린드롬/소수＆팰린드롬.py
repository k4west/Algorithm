n=int(input())
if n==1 or n==2:
    print(2)
else:
    while True:
        if n%2:
            for i in range(3, int(n**.5)+1):
                if n%i==0:
                    break
            else:
                for i in range(len(s:=str(n))//2):
                    if s[i] != s[-i-1]:
                        break
                else:
                    print(n)
                    exit()
        n+=1