def main():
    a,b=open(0).readlines()
    s=1
    for i in sorted(map(int,b.split())):
        if s==i:s+=1
        else:print(s);return
    print(s)
main()