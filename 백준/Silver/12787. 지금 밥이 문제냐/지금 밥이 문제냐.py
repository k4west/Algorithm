def main():
    a=open(0);T=[]
    for _ in range(int(next(a))):
        M,N=next(a).split()
        if M=='1':T.append(sum(n<<(56-8*i) for i,n in enumerate(map(int,N.split('.')))))
        else:
            t,N=[],int(N)
            for _ in range(8):t.append(N%256);N>>=8
            T.append('.'.join(map(str,t[::-1])))
    print('\n'.join(map(str,T)))
main()