n=int(input())
m=(n-3)//2
b,s,e='|* '
t=[b+'-'*(n-2)+b]+[b+e*i+s+e*(n-4-2*i)+s+e*i+b for i in range(m)]
t+=[b+e*m+s+e*m+b]+t[::-1]
print('\n'.join(t))