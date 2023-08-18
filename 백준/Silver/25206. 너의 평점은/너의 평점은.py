l=[]
for i in range(20):
    l.append(list(map(str,input().split(" "))))
t={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
g,s=0,0
for i in range(len(l)):
    if l[i][2]!="P":
        s+=float(l[i][1])
        g+=float(l[i][1])*t[l[i][2]]
print(g/s)