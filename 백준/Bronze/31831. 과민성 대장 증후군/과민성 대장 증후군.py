import sys
def main():
    input=sys.stdin.readline
    N,M=map(int,input().split())
    s=d=0
    for m in map(int,input().split()):
        if (s:=max(s+m,0))>=M:d+=1
    print(d)
main()