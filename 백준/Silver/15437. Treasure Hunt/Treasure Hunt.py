def main():
    r,c=map(int, input().split())
    arr=[list(input()) for _ in range(r)]
    i=j=moves=0
    visited=[[False] * c for _ in range(r)]
    out=False
    while True:
        direction=arr[i][j]
        if direction=='E':
            j+=1
            if j >= c:out=True
        elif direction=='W':
            j-=1
            if j < 0:out=True
        elif direction=='S':
            i+=1
            if i >= r:out=True
        elif direction=='N':
            i-=1
            if i < 0:out=True
        elif direction=='T':print(moves);return
        if out:print("Out");break
        if visited[i][j]:print("Lost");break
        else:visited[i][j]=True
        moves+=1
if __name__=="__main__":
    main()