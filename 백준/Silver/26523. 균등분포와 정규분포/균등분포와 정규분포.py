n=u=0
for i,j in enumerate(map(float,open(0).read().split()),1):
    if 0.25<=j<=0.75:n+=1
    if not i%5000:print('AB'[n>2600]);n=u=0