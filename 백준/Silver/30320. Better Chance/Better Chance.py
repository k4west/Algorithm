import sys
rt, rj, st, sj = sys.stdin.readline().split()
t, j = (int(rt)-1)*int(float(sj)*100+0.5),(int(rj)-1)*int(float(st)*100+0.5)
if t < j: print("TAOYUAN")
elif t > j: print("JAKARTA")
else: print("SAME")