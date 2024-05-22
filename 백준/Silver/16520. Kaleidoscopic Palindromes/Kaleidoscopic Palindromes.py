def main():
    a,b,k=map(int,input().split())
    s=0
    for i in range(a,b+1):
        f=False
        for j in range(2,k+1):
            t=i
            tmp=[]
            while t:
                tmp.append(t%j)
                t//=j
            for t in range(len(tmp)//2):
                if tmp[t]!=tmp[-t-1]:
                    f=True
                    break
            if f:break
        if not f:s+=1
    print(s)
main()