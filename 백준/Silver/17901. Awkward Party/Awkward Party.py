def main():
    n,*a=map(int, open(0).read().split())
    d={}
    for i in range(n):
        if (g:=a[i]) in d and n>(t:=i-d[g]):n=t
        d[g]=i
    print(n)
main()