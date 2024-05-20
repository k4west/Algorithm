p=q=''
c=0
for i in input():
    if i=='M':c+=1
    elif c:p+='5'+'0'*c;q+='1'+'0'*(c-1)+'5';c=0
    else:p+='5';q+='5'
if c:p+='1'*c;q+='1'+'0'*(c-1)
print(f'{p}\n{q}')