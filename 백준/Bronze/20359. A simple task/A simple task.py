n=bin(int(input()))[2:]
o=n.rstrip('0')
print(int(o,2), len(n)-len(o))