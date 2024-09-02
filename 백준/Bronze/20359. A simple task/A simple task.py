n=bin(int(input()))
o=n.rstrip('0')
print(int(o[2:],2), len(n)-len(o))