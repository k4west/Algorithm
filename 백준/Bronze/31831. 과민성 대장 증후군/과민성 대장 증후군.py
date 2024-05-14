def main():
    N,M=map(int,input().split())
    s=d=0
    for m in map(int,input().split()):
        s+=m
        if s<0:s=0
        if s>=M:d+=1
    print(d)
main()