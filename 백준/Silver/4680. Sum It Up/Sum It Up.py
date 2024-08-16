def f(s,idx,arr):
    if s>total:return
    if s==total:
        if arr not in tmp:tmp.append(arr)
        return
    if idx==n:return
    e=x[idx]
    f(s+e,idx+1,arr+[e])
    f(s,idx+1,arr)
a=open(0)
ans=[]
for i in a:
    total,n,*x=map(int,i.split())
    if total==0:break
    tmp=[]
    f(0,0,[])
    if not tmp:tmp=['NONE']
    else:tmp=map(lambda x: '+'.join(map(str,x)),tmp)
    ans.append(f'Sums of {total}:\n'+'\n'.join(tmp))
print('\n'.join(ans))