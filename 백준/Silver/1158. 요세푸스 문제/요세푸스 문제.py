n,k=map(int,input().split())
arr=[*range(1,n+1)]
i=0
ans=[str(arr.pop(i:=(i+k-1)%(n-j))) for j in range(n)]
print(f'<{", ".join(ans)}>')