import sys
def main():
    input=sys.stdin.readline
    N,x=int(input()),int(input())
    N2=N*N
    td,M=[[N2-i]+[0]*(N-1) for i in range(N)],(N-1)//2
    r=c=M
    if x in range(N*(N-1)+1,N2+1): r,c=N2-x,0
    t=1
    for i in range(N):
        prev=td[i][0]
        if i==M: t=0
        for j in range(1,N):
            num=1
            if j<=i+t:
                if t or i!=N-1 and j<=M-i%M: num=(N-2*j+1)*4-1
                num*=-1
            elif N-j<=(i*t)-(2*M-i)*(t-1): num=(2*j-N)*4-1
            prev=td[i][j]=prev+num
            if prev==x: r,c=i,j
    print("\n".join(map(lambda x:" ".join(map(str,x)),td)))
    print(r+1,c+1)
main()