n,k=map(int,input().split())
arr=[*range(1,n+1)]
ans=[]
i=0
for j in range(n):
    ans.append(arr.pop(i:=(i+k-1)%(n-j)))
print(f'<{", ".join(map(str,ans))}>')