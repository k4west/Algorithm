import sys
rt,rj,st,sj=map(float,sys.stdin.readline().split())
t,j=(rt-1)*int(sj*1000),(rj-1)*int(st*1000)
if t<j: print("TAOYUAN")
elif t>j: print("JAKARTA")
else: print("SAME")