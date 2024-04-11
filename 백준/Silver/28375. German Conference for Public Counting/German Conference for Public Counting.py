a=((l:=len(n:=input()))-1)*10+int(t:=n[0])
if n<t*l:a-=1
if l==1:a+=1
print(a)