x=int(input())
y=int(input())
q=1
if x>0:
    if y<0:
        q=4
elif y>0:
    q=2
else:q=3
print(q)