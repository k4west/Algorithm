import sys
X,Y=map(int,sys.stdin.readline().split())
if(Z:=(Y*100)//X)>=99:print(-1)
else:print(bool(((Y+(i:=(X *(Z+1)-100*Y)//(99-Z)))*100)//(X+i)<=Z)+i)