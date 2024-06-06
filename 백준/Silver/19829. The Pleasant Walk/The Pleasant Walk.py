a=open(0)
def main():
    n,k=map(int,next(a).split())
    c=next(a).split()
    v=[i for i in range(n)]
    for i in range(n-1):
        if c[i]!=c[i+1]:v[i+1]=v[i]
    d={}
    for i in v:d[i]=d.get(i,0)+1
    print(max(d.values()))
main()