def main():
    _,a,b=open(0)
    d=[0]*(10**6+1)
    for i in map(int,b.split()):d[i]+=1
    for i in map(int,a.split()):
        if d[i]:d[i]-=1
    print(sum(d))
main()