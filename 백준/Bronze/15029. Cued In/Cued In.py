d={'red':1,'yellow':2,'green':3,'brown':4,'blue':5,'pink':6,'black':7}
t=[d[i.strip()] for i in open(0).readlines()[1:]]
if (s:=t.count(1))==len(t):print(1)
else:print(sum(t)+max(t)*s)