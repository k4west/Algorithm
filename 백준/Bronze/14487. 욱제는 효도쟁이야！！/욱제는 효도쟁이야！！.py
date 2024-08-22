def main():
    n,a=open(0)
    m=s=0
    for i in map(int,a.split()):
        if m<i:m=i
        s+=i
    print(s-m)
main()