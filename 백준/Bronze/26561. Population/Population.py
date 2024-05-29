def main():
    T=[]
    for _ in range(int(input())):p,t=map(int,input().split());T.append(p+t//4-t//7)
    print(*T,sep='\n')
main()