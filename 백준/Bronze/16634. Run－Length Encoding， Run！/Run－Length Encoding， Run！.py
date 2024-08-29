a,s=input().split()
r=''
if a=='E':
    t,c='',0
    for i in s:
        if i!=t:
            if c:r+=f'{t}{c}';c=0
            t=i
        c+=1
    r+=f'{t}{c}'
else:
    for i in range(0,len(s),2):r+=s[i]*int(s[i+1])
print(r)