input()
Y=M=0
for n in map(int, input().split()):
    Y+=n//30*10+10
    M+=n//60*15+15
if Y==M:print(f'Y M {Y}')
elif Y<M:print(f'Y {Y}')
else:print(f'M {M}')