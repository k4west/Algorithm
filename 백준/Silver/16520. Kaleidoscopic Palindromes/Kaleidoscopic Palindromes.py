def check(n, b):
    tmp=[]
    while n:
        tmp.append(n%b)
        n//=b
    for i in range(len(tmp)//2):
        if tmp[i] != tmp[-i-1]:
            return False
    return True
a,b,k=map(int,input().split())
s=0
for i in range(a,b+1):
    s+=all(check(i,j) for j in range(2,k+1))
print(s)