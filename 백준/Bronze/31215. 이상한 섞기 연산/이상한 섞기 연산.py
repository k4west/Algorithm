_,*a=map(float,open(0).read().split())
print('\n'.join(map(str,[2*(m>2)+1 for m in a])))