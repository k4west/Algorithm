m=1040
p=[0]+[1]*1040
for i in range(2,33):
    if p[i]:
        for j in range(i*i, m+1, i):
            p[j]=0
d={chr(i+96) if i < 27 else chr(i+38):i for i in range(1,53)}
s=sum(d[s] for s in open(0).read().strip())
t = ['not ', ''][p[s]]
print(f'It is {t}a prime word.')