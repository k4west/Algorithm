def main():
    a=[]
    for i in open(0):
        n,w,d,s=map(int,i.split())
        t=n*(n-1)*w//2-s
        a.append([n,t//d][bool(t)])
    print('\n'.join(map(str,a)))
main()