def main():
    input()
    a=input().replace('V', ' ').split()
    r=1
    for i in a:
        t,m=1,len(i)-1
        for j in range(m):
            if i[j]!=i[j+1]:t+=1
            else:r=max(r,t);t=1
    print(max(r,t))
main()