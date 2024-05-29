def main():
    a=open(0);T=[]
    for _ in range(int(next(a))):
        next(a);s=sum(t:=[*map(int,next(a).split())]);m=1
        for i in t:
            m*=i
            if m>s:print('ILOCZYN');break
        else:print('SUMA' if s>m else '=')
    print(*T,sep='\n')
main()