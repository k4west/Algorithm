import sys

def main():
    ans=[]
    d=[False]*(1001)
    for n in sys.stdin.readlines()[1:]:
        if not d[(n:=int(n))]:
            cnt=0
            for b in range(2,n+1):
                s=n
                while not s%b:cnt+=1;s//=b
            d[n]=str(cnt)
        ans.append(d[n])
    print("\n".join(ans))

if __name__=="__main__":
    main()