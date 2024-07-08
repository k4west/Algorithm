n,s=open(0)
s=s.strip()
print(sum(s[i]!=s[-i-1] for i in range(int(n)//2)))