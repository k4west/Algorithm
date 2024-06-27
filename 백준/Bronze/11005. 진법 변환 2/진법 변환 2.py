N,B=map(int,input().split())
t=[]
while N:
    i=N%B
    t.append(chr(i+55) if i>9 else i)
    N//=B
print(*t[::-1],sep='')