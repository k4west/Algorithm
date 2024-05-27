def main():
    a=open(0).readlines()
    i,T=0,[]
    while i<len(a):
        _,L,C=map(int,a[i].split())
        t=l=0;c=-1;f=False
        for j in map(len,a[i+1].split()):
            if (c:=c+j+1)>C:
                c=j;l+=1
                if l==L:l=0;t+=1
        T.append(t+1);i+=2
    print('\n'.join(map(str,T)))
main()