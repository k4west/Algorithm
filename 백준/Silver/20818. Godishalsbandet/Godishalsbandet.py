def main():
    a=[i=='B' for i in input()]
    n=len(a)
    h=n//2
    m=c=sum(a[:h])
    for i in range(n):
        c+=a[(h+i)%n]-a[i]
        if m<c:
            m=c
    print(m)
main()