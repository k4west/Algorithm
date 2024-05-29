def main():
    a=open(0);T=[]
    for _ in range(int(next(a))):
        next(a);s=sum(t:=[*map(int,next(a).split())]);m=1
        for i in t:
            m*=i
            if m>s: T.append('ILOCZYN');break
        else:T.append(['=','SUMA'][s>m])
    print(*T,sep='\n')
main()